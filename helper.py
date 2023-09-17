import datetime
import io
import csv
from dataclasses import dataclass

items = []


@dataclass
class Item:
    text: str
    date: datetime
    category: str
    description: str
    isCompleted: bool = False


def oneWeekFromToday():
    today = datetime.datetime.now()
    oneWeek = datetime.timedelta(weeks=1)
    return today + oneWeek


def add(text, date=None, category=None, description=None):
    text = text.replace("b", "bbb").replace("B", "Bbb")
    if date is None:
        date = oneWeekFromToday()
    else:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")

    if category is None:
        category = "default"

    if description is None:
        description = ""
    items.append(Item(text, date, category, description))
    items.sort(key=lambda x: (x.date, x.category))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted


def get_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Titel", "Datum", "Kategorie", "Beschreibung", "Erledigt?"])
    for item in items:
        writer.writerow(
            [
                item.text,
                item.date.strftime("%d.%m.%Y"),
                item.category,
                item.description,
                "x" if item.isCompleted else "o",
            ]
        )
    return output.getvalue()
