from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    # Kivy App for converting miles to kilometres
    output_km = StringProperty()

    def build(self):
        # Build the Kivy app using the kv file.
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        # This function will handle the calculation
        print("handle calculate")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        # This function will handle the increments from miles to km.
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * FACTOR_MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        # This will convert text to float or 0.0 if invalid.
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()