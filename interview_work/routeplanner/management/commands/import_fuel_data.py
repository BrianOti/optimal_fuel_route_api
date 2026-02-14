import pandas as pd
from django.core.management.base import BaseCommand
from routeplanner.models import FuelStation

class Command(BaseCommand):
    help = "Import fuel data from CSV"

    def handle(self, *args, **kwargs):
        df = pd.read_csv("fuel_prices_full_output.csv")

        for _, row in df.iterrows():
            FuelStation.objects.create(
                opis_id=row["OPIS Truckstop ID"],
                name=row["Truckstop Name"],
                address=row["Address"],
                city=row["City"],
                state=row["State"],
                rack_id=row["Rack ID"],
                retail_price=row["Retail Price"]
            )

        self.stdout.write(self.style.SUCCESS("Fuel data imported successfully"))
