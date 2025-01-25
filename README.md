# Scheduler
Simple app for creating and viewing scheduled events. The backend uses Django and the frontend uses React.

## Backend
### Local Development
1. In `scheduler-backend/scheduler`, run `python3 -m venv env` and activate the virtual environemtn.
2. Install the requirements with `pip install -r requirements.txt`
3. Run migrations with `python3 manage.py migrate`
4. Create a super user with `python3 manage.py createsuperuser`. You will use this user to create events for the time being.
5. Run the server with `python3 manage.py runserver`
6. Go to http://127.0.0.1:8000/admin and login with the user you just created.
7. Go to "Events" and click "Add". Add as many events as you would like. To add a repeating day to an event, you will also need to create the required day through "Days" and "Add".


### Features
The backend currently supports creating events and returning a list of events within a date range. The backend supports flagging these events as repeating weekly on particular days, but the front end does not yet use this information.

The backend does not currently support validating that events do not overlap.

### Future Enhancements
- Add support for deleting events.
- Add support for editing an existing event.

## Frontend
### Local Development
1. In `scheduler-frontend/scheduler`, run `npm install`
2. Start the server with `npm run dev`
3. Go to http://localhost:3000 to view the app.

### Features
The frontend currently supports viewing events. It is not yet utilizing the backend's ability to filter events by a date range. Instead, it's currently displaying all events.

The frontend does not yet support creating events. Until this feature is implemented, events can be created in the Django admin.

### Future Enhancements
- Add support for deleting events.
- Add support for editing existing events.
- Create a daily and weekly layout that shows events in a calendar-like structure instead of a list.
