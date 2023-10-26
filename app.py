import streamlit as st
import ssl
from PIL import Image
from urllib.request import urlopen

ssl._create_default_https_context = ssl._create_unverified_context

custom_css = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
                background-image: url('https://i.postimg.cc/jqvTs0yP/CDS.png');
                background-repeat: no-repeat;
                background-size: cover;
                background-position: center;
            }
            .stApp {
                width: 750px;
                height: 850px;
                background-color: rgba(255, 255, 255, 0.85);
                border: 8px solid #2470a0; 
                border-radius: 20px;
                padding: 10px; 
                margin: 10px 0;
                transform: translate(-50%, -50%);
                left: 50%;
                top: 50%;
            }
            h1 {
                color: black;
            }
            .big-label {
                color: black;
                font-family: 'Roboto', sans-serif;
                font-size: 2.5em;
                font-weight: bold;
            }
            .output {
                border-style: solid;
                border-width: 3.5px;
                border-radius: 10px;
                display: flex;
                justify-content: center;
                align-items: center;
                color: black;
                font-size: 2em;
                font-weight: bold;
            }
            </style>
            """
st.markdown(custom_css, unsafe_allow_html=True)

imageLOGO = Image.open(urlopen("https://i.ibb.co/WGjVK32/logopng.png"))
st.image(imageLOGO)
def calculate_weight(device):
    weights = {
        'Arrow - device only': 0.1,
        'Dagger Slim / Dagger Large': 0.5,
        'Harness Only': 0.3,
        'Arrow with harness': 0.5,
        'EVO - device only': 0.1,
        'REVO': 0.5,
        'EVO with harness': 0.5,
    }
    
    return weights[device]

def calculate_labels_and_weight(device, qty, shipping_type):
    weights = {
        'Arrow - device only': 0.1,
        'Dagger Slim / Dagger Large': 0.5,
        'Harness Only': 0.3,
        'Arrow with harness': 0.5,
        'EVO - device only': 0.1,
        'REVO': 0.5,
        'EVO with harness': 0.5,
    }
    
    weight_per_device = weights.get(device, 0)  # Get the weight for the specified device
    labels = []

    if shipping_type == "New Car":
        total_boxes = qty // 50
        remaining = qty % 50

        per_box_weight = 50 * weight_per_device

        if total_boxes:
            labels.append(f"({total_boxes}) Labels @ {per_box_weight:.2f} lbs EACH")
        if remaining:
            labels.append(f"(1) Label @ {(remaining * weight_per_device):.2f} lbs")

    elif shipping_type == "BHPH":
        boxes_20 = qty // 20
        remaining_20 = qty % 20
        boxes_10 = remaining_20 // 10
        remaining_10 = remaining_20 % 10

        per_box_weight_20 = 20 * weight_per_device
        per_box_weight_10 = 10 * weight_per_device

        if boxes_20:
            labels.append(f"({boxes_20}) Labels @ {per_box_weight_20:.2f} lbs EACH")
        if boxes_10:
            labels.append(f"({boxes_10}) Labels @ {per_box_weight_10:.2f} lbs EACH")
        if remaining_10:
            labels.append(f"(1) Label @ {(remaining_10 * weight_per_device):.2f} lbs")

    return ' and '.join(labels)


def main():
    st.title("RMA Weight Calculator")
    
    shipping_type = st.selectbox("Please select:", ['New Car', 'BHPH'])
    
    if shipping_type == "New Car":
        device_options = ['Arrow with harness', 'Dagger Slim / Dagger Large', 'Harness Only', 'Arrow - device only']
    else:
        device_options = ['EVO with harness', 'REVO', 'Harness Only', 'EVO - device only']
    device = st.selectbox("Select Item(s) Type:", device_options)
    
    qty = st.text_input("Enter the quantity of item(s) being returned:", value="1")
    
    if not qty.isdigit():
        st.warning("Please enter a valid quantity.")
        return
    
    labels = calculate_labels_and_weight(device, int(qty), shipping_type)
    
    st.markdown(f'<div class="output"> {labels}</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
