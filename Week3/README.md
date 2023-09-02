# Week 3

## Frequency Domain - Discrete Cosine Transfrom technique

Set up Python environment with Anaconda

    conda create --name python3.8 python=3.8

    conda activate python3.8

Install required library

    pip install scikit-image

Run hiding secret image in the cover image

    python DCT_hide.py <cover_image_path> <secret_imate_path>

E.g: python DCT_hide.py test.png watermark.jpg --> This will create new output file (contains secret image)

Reveal the secret image from stego image
   
    python DCT_reveal.py <stego_image_path>

E.g: python DCT_hide.py output.png --> This will result in creating new stego_image (without any file extension)
