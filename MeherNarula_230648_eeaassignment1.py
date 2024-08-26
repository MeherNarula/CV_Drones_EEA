import cv2
import numpy as np

def resize_image(image, size=(256, 256)):
    return cv2.resize(image, size)

def ideal_filter(rows, cols, cutoff_frequency, filter_type='lpf'):
    mask = np.zeros((rows, cols), dtype=np.uint8)
    center_row, center_col = rows // 2, cols // 2

    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - center_row) ** 2 + (j - center_col) ** 2)

            if filter_type == 'lpf' and distance <= cutoff_frequency:
                mask[i, j] = 1
            elif filter_type == 'hpf' and distance > cutoff_frequency:
                mask[i, j] = 1

    return mask

def apply_filter(image, filter_mask):
    f_transform = np.fft.fft2(image)
    f_transform_shifted = np.fft.fftshift(f_transform)

    # Apply the filter mask
    f_transform_filtered = f_transform_shifted * filter_mask

    # Inverse FFT to get back the image in spatial domain
    f_transform_inverse = np.fft.ifftshift(f_transform_filtered)
    image_filtered = np.fft.ifft2(f_transform_inverse)
    image_filtered = np.abs(image_filtered)

    return image_filtered

def main(s1, s2, cutoff_frequency):
    # Read and resize the input images
    image1 = resize_image(cv2.imread(s1, cv2.IMREAD_GRAYSCALE))
    image2 = resize_image(cv2.imread(s2, cv2.IMREAD_GRAYSCALE))

    # Get the dimensions of the images
    rows, cols = image1.shape

    # Create Ideal LPF and HPF filters
    lpf_filter = ideal_filter(rows, cols, cutoff_frequency, filter_type='lpf')
    hpf_filter = ideal_filter(rows, cols, cutoff_frequency, filter_type='hpf')

    # Apply LPF and HPF on each image
    image1_lpf = apply_filter(image1, lpf_filter)
    image2_hpf = apply_filter(image2, hpf_filter)

    # Average the two filtered images
    hybrid_image = (image1_lpf + image2_hpf) / 2

    # Display results
    cv2.imshow('Original Image 1', image1)
    cv2.imshow('Original Image 2', image2)
    cv2.imshow('Ideal LPF Filter', lpf_filter * 255)
    cv2.imshow('Fourier of Image 1', np.log1p(np.abs(np.fft.fftshift(np.fft.fft2(image1)))))
    cv2.imshow('Fourier after LPF', np.log1p(np.abs(np.fft.fftshift(np.fft.fft2(image1_lpf)))))
    cv2.imshow('Modified Image after LPF', np.uint8(image1_lpf))
    cv2.imshow('Combined Hybrid Image', np.uint8(hybrid_image))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
s1 = "C:\important downloads\galaxy.webp"  # Replace with the actual path of the first image
s2 = "C:\important downloads\headphones.webp"  # Replace with the actual path of the second image
cutoff_frequency = 30  # Adjust as needed

main(s1, s2, cutoff_frequency)