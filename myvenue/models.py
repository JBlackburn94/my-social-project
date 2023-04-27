from myvenue import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(50), unique=True, nullable=False)
    events = db.relationship(
        "Event_Details", backref="event", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.event_name


class Event_Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(50), unique=True, nullable=False)
    venue_name = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey(
        "event.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return "#{0} - Event {1} | Venue: {2} | City: {3} | Date: {4}".format(
            self.id, self.artist_name, self.venue_name, self.city, self.date
        )
