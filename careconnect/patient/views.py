import calendar
from collections import defaultdict
from datetime import datetime

from django.views import View
from django.shortcuts import render

from treatment.models import PatientMedicine, Appointment

class PatientMedicineView(View):
    template_name = 'patient.html'

    def get(self, request, year=None, month=None):
        patient_id = 5  # Example patient ID
        appointment = Appointment.objects.filter(patient=patient_id)

        patient_medicines = PatientMedicine.objects.filter(patient=patient_id)

        # Get the current date or the date based on provided year and month
        today = datetime.today()
        year = year or today.year
        month = month or today.month

        # Adjust for month overflow (if user navigates to the next/previous year)
        if month < 1:
            month = 12
            year -= 1
        elif month > 12:
            month = 1
            year += 1

        # Generate calendar for the given month and year
        cal = calendar.TextCalendar(calendar.SUNDAY)
        month_calendar = cal.monthdayscalendar(year, month)

        # Get the start and end date of the month
        start_date = datetime(year, month, 1)
        last_day = calendar.monthrange(year, month)[1]  # Get the number of days in the month
        end_date = datetime(year, month, last_day)

        # Filter appointments for the given month and year
        appointments_in_month = Appointment.objects.filter(
            patient=patient_id,
            date__year=year,
            date__month=month
        )

        # Create a dictionary to store appointments for each day
        appointments_by_day = defaultdict(list)
        for appt in appointments_in_month:
            appointments_by_day[appt.date.day].append(appt)

        # Modify the calendar to include appointments for each day
        calendar_with_appointments = []
        for week in month_calendar:
            week_with_appointments = []
            for day in week:
                if day != 0:  # If day is 0, it means it's a blank day in the calendar
                    day_appointments = appointments_by_day.get(day, [])
                    week_with_appointments.append({
                        'day': day,
                        'appointments': day_appointments
                    })
                else:
                    week_with_appointments.append({'day': 0, 'appointments': []})
            calendar_with_appointments.append(week_with_appointments)

        # Get the month name (e.g., "January", "February")
        month_name = calendar.month_name[month]

        # Pass the calendar and other details to the template
        context = {
            'year': year,
            'month': month,
            'month_name': month_name,
            'month_calendar': calendar_with_appointments,  # Updated calendar with appointments
            'appointments_by_day': appointments_by_day,    # Raw appointment data, if needed
        }

        return render(request, self.template_name, context)
