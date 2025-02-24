import os
from taipy import Gui
from flask import Flask, send_file
from flask_cors import CORS
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer

# Create a Taipy GUI
gui = Gui("<|This Page is meant to give access to the COA of the CBD offered, and subject to change without notice depending on the harvest season.|>")


nav_menu = """
# Navigation Menu
* [COA Page](/pdf)
* [Warning/Directions Page](/warning)
* [Business Opportunity/Survey](https://docs.google.com/forms/d/e/1FAIpQLSeFQwgFouHuj6qauAXjab5po0jKMM030eiOLi0gKuxtTtGUHw/viewform)
"""


# Make /nav the default page
# Add the navigation menu to the GUI
gui.add_page("nav", nav_menu)


# Define the Markdown content of the page
pdf_page = """
# COA Page can be gotten at link below
You can view the COA at the following link and download: [here](http://ai-claude-opensource.onrender.com/pdf/IHPUSA_COA.pdf).
"""

# Add a new page to the GUI
gui.add_page("pdf", pdf_page)

# Create a Flask app to serve the PDF
app = Flask(__name__)
CORS(app)


@app.route("/pdf")
def serve_pdf():
    # Ensure the file path is correct
    return send_file(r'C:\Users\Solid\OneDrive\Documents\GitHub\AI_Claude_OpenSource\pdf\IHPUSA_COA.pdf', as_attachment=False)


@app.route("/warning")
def serve_warning():
    return gui.get_page("warning")


# Create a Taipy Markdown page with the warning text
data = f"""
This page is meant to give access to the COA of the CBD offered and is subject to change without notice depending on the harvest season.

### IHPUSA Product Warning QR Code
Scan this QR code to view the product warning information.

### Product Warning
**WARNING:** For external use only.
- Highly Flammable: Keep away from heat, sparks, electrical sources, fire, or flame.
- Avoid contact with eyes: It can cause serious eye irritation.
- Inhalation hazard: May cause drowsiness and dizziness.
- Do not ingest: Can cause serious gastric disturbances if taken internally.
- **WARNING:** KEEP OUT OF REACH OF CHILDREN AND PETS and don't use on finished floor surfaces (e.g., ceramic tile).
- **EYE IRRITANT:** Avoid contact with eyes. If eye contact occurs, rinse with water. If irritation persists, contact a physician.

### Instructions
- Do not spray on or permit contact with fabrics, painted surfaces, or finished surfaces.
- Do not spray in automobiles or confined areas.
- Shake well before using.
- Keep in a cool, dry space.
- Avoid prolonged exposure to sun.
- Shake well before using.

### Ingredients
- All Natural Products - Proprietary Information

### Cautions and Warnings
- For external use only.
- Do not spray on or permit contact with fabrics, painted surfaces, or finished surfaces which may cause slippery surfaces.
- The product is flammable.
- May irritate skin. Discontinue use if irritation or rash occurs.
- Avoid contact with eyes, ears, mouth, and open cuts or wounds, even when diluted.
- Keep out of children’s reach to avoid accidental ingestion or inhalation, which can cause serious injury.
- Consult a doctor immediately if breathing problems occur.
- Consult a physician before use if pregnant, nursing, taking medication, or suffering from a medical condition.
- This product may stain due to its strong pigment.

### Contact Information
K&L Manufacturing  
IHPUSA Distribution: 757-271-1576  
Organic CBD Grown in VA, USA 
"""

# Add the warning page to the GUI
gui.add_page("warning", data)

# Generate a QR code with the warning information
try:
    qr = qrcode.QRCode(
        version=7,  # Set a specific version that you know will fit the data
        error_correction=qrcode.constants.ERROR_CORRECT_H,
    )
    qr.add_data(data)
    qr.make(fit=True)
    # Create an image from the QR Code instance
    img = qr.make_image(image_factory=StyledPilImage,
                        module_drawer=GappedSquareModuleDrawer())
    # Save the image
    img.save("ihpusa_qrcode.png")
except ValueError as e:
    print(f"Error creating QR code: {e}")


@app.route("/")
def index():
    return redirect(url_for("serve_nav"))

# Serve the navigation menu


@app.route("/nav")
def serve_nav():
    return gui.get_page("nav")


# Run the Taipy GUI
if __name__ == '__main__':
    import threading
    # Start Flask server in a separate thread
    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=5001)).start()
    port = int(os.environ.get("PORT", 5000))
    gui.run(host="0.0.0.0", port=port)
