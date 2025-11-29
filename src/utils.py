import os

def save_yaml(content, input_filename, output_dir):
    """
    Saves string content to a YAML file in the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Change extension from .jpg/.png to .yaml
    base_name = os.path.splitext(os.path.basename(input_filename))[0]
    output_path = os.path.join(output_dir, f"{base_name}.yaml")

    with open(output_path, "w") as f:
        f.write(content)
    
    print(f"✅ Saved YAML to: {output_path}")