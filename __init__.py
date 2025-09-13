import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class FillerWireApp(toga.App):

    def startup(self):
        """Construct and show the Toga application."""
        
        # Create a main box that will hold all widgets
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Title
        self.title_label = toga.Label("🔧 Filler Wire Calculator 🔧", style=Pack(font_size=20))
        main_box.add(self.title_label)

        # Tube diameter input
        self.diameter_input = toga.Selection(items=["15.875", "19.05", "22.225", "25.4"], style=Pack(width=200))
        self.diameter_input.label = "Tube Diameter (mm)"
        main_box.add(self.diameter_input)

        # Tube projection input
        self.projection_input = toga.Selection(items=["1", "1.5", "2", "3"], style=Pack(width=200))
        self.projection_input.label = "Projection (mm)"
        main_box.add(self.projection_input)

        # Filler wire size input
        self.filler_size_input = toga.Selection(items=["1.6mm", "2.4mm"], style=Pack(width=200))
        self.filler_size_input.label = "Filler Wire Size"
        main_box.add(self.filler_size_input)

        # Tubes entry
        self.tubes_input = toga.TextInput(style=Pack(width=200))
        self.tubes_input.placeholder = "Enter Total Tubes"
        main_box.add(self.tubes_input)

        # Calculate Button
        self.calculate_button = toga.Button("Calculate", on_press=self.calculate_filler_wire)
        main_box.add(self.calculate_button)

        # Results display
        self.result_filler_wires = toga.Label("Total Filler Wires: ", style=Pack(font_size=16))
        self.result_weight = toga.Label("Total Weight (kg): ", style=Pack(font_size=16))
        main_box.add(self.result_filler_wires)
        main_box.add(self.result_weight)

        # Set the content of the main window
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def calculate_filler_wire(self, widget):
        """Perform the filler wire calculation and display the results."""
        try:
            # Get input values
            diameter = float(self.diameter_input.value)
            projection = float(self.projection_input.value)
            filler_wire_size = self.filler_size_input.value
            total_tubes = int(self.tubes_input.value)

            # Fixed values
            length_of_filler_wire = 500.0
            scrap_length = 120.0

            # Filler wire weight based on size
            if filler_wire_size == "1.6mm":
                weight_of_filler_wire = 0.015
            elif filler_wire_size == "2.4mm":
                weight_of_filler_wire = 0.021
            else:
                self.result_filler_wires.text = "Invalid Filler Wire Size"
                return

            # Projection factor
            projection_factor = 1 + (projection * 0.15)

            # Filler wire needed per tube
            filler_wire_per_tube = (diameter * 3.14159) * 1.2
            filler_wire_per_tube_adjusted = filler_wire_per_tube * projection_factor

            # Tubes welded per filler wire
            tubes_welded_per_wire = (length_of_filler_wire - scrap_length) / filler_wire_per_tube_adjusted

            # Total filler wires required
            total_filler_wires = total_tubes / tubes_welded_per_wire

            # Total weight
            total_weight = total_filler_wires * weight_of_filler_wire

            # Display results
            self.result_filler_wires.text = f"Total Filler Wires: {total_filler_wires:.2f}"
            self.result_weight.text = f"Total Weight (kg): {total_weight:.3f}"

        except ValueError:
            self.result_filler_wires.text = "Error: Invalid input"
            self.result_weight.text = "Please enter valid numerical values."


def main():
    return FillerWireApp("Filler Wire Calculator", "com.yourname.fillerwirecalc")


if __name__ == '__main__':
    main()
# Trigger GitHub Actions build
