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

        if total_boxes:
            labels.append(f"({total_boxes}) Label{'s' if total_boxes > 1 else ''} @ {(total_boxes * 50 * weight_per_device):.2f} lbs each")
        if remaining:
            labels.append(f"(1) Label @ {(remaining * weight_per_device):.2f} lbs")

    elif shipping_type == "BHPH":
        boxes_20 = qty // 20
        remaining_20 = qty % 20
        boxes_10 = remaining_20 // 10
        remaining_10 = remaining_20 % 10

        if boxes_20:
            labels.append(f"({boxes_20}) Label{'s' if boxes_20 > 1 else ''} @ {(boxes_20 * 20 * weight_per_device):.2f} lbs each")
        if boxes_10:
            labels.append(f"({boxes_10}) Label{'s' if boxes_10 > 1 else ''} @ {(boxes_10 * 10 * weight_per_device):.2f} lbs each")
        if remaining_10:
            labels.append(f"(1) Label @ {(remaining_10 * weight_per_device):.2f} lbs")

    return ' and '.join(labels)

# Test with a quantity of 125 of "Arrow with harness" for shipping type "New Car"
result = calculate_labels_and_weight("Arrow with harness", 125, "New Car")
print(result)
