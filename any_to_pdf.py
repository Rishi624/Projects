import os
import sys
import io
import shutil
import tempfile
from tkinter import filedialog, Tk, messagebox
from PIL import Image
from docx2pdf import convert as docx_convert
from reportlab.pdfgen import canvas
from PyPDF2 import PdfMerger
import comtypes.client  # Import for PowerPoint conversion

# ✅ Fix for Unicode print support in Windows terminal
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def txt_to_pdf(txt_path, pdf_path):
    c = canvas.Canvas(pdf_path)
    with open(txt_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i > 50:
                break  # avoid writing too far down the page
            c.drawString(50, 800 - 15 * i, line.strip())
    c.save()

def image_to_pdf(img_path, pdf_path):
    img = Image.open(img_path).convert('RGB')
    img.save(pdf_path)

def ppt_to_pdf(ppt_path, pdf_path):
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    try:
        presentation = powerpoint.Presentations.Open(ppt_path, WithWindow=False)
        # Remove .pdf extension from pdf_path (PowerPoint adds it automatically)
        if pdf_path.lower().endswith(".pdf"):
            pdf_path = pdf_path[:-4]
        presentation.SaveAs(pdf_path, 32)  # 32 = PDF format
        print(f"✅ Converted PPT to PDF: {ppt_path} -> {pdf_path}.pdf")
        presentation.Close()
    except Exception as e:
        print(f"❌ Failed to convert {ppt_path}: {e}")
    finally:
        powerpoint.Quit()


def images_to_single_pdf(image_paths, output_pdf_path):
    images = []
    for path in image_paths:
        img = Image.open(path).convert('RGB')
        images.append(img)
    if images:
        images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
        print(f"✅ PDF saved to {output_pdf_path}")
    else:
        print("❌ No images to convert.")

def handle_conversion(file_path, output_folder, temp_dir=None):
    ext = os.path.splitext(file_path)[1].lower()
    filename = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(output_folder, f"{filename}.pdf") if not temp_dir else os.path.join(temp_dir, f"{filename}.pdf")

    try:
        if ext in ['.jpg', '.jpeg', '.png']:
            image_to_pdf(file_path, output_path)
        elif ext == '.txt':
            txt_to_pdf(file_path, output_path)
        elif ext == '.docx':
            if temp_dir:
                # docx2pdf only supports folder output, so use temp_dir
                docx_convert(file_path, temp_dir)
            else:
                docx_convert(file_path, output_folder)
        elif ext in ['.ppt', '.pptx']:
            ppt_to_pdf(file_path, output_path)
        elif ext == '.pdf':
            if temp_dir:
                shutil.copy(file_path, output_path)
            else:
                shutil.copy(file_path, output_path)
        else:
            messagebox.showerror("Unsupported File", f"Cannot convert '{ext}' files.")
            return None
        print(f"✅ Converted: {file_path} -> {output_path}")
        return output_path
    except Exception as e:
        print(f"❌ Failed to convert {file_path}: {e}")
        return None

def merge_pdfs(pdf_paths, output_pdf_path):
    merger = PdfMerger()
    for pdf in pdf_paths:
        merger.append(pdf)
    merger.write(output_pdf_path)
    merger.close()
    print(f"✅ Merged PDF saved to {output_pdf_path}")

def main():
    root = Tk()
    root.withdraw()  # Hide the main Tk window

    file_paths = filedialog.askopenfilenames(title="Select files to convert")
    if not file_paths:
        print("❌ No files selected.")
        return

    output_folder = filedialog.askdirectory(title="Select folder to save PDFs")
    if not output_folder:
        print("❌ No output folder selected.")
        return

    if len(file_paths) == 1:
        # Single file: behave as before
        handle_conversion(file_paths[0], output_folder)
    else:
        # Multiple files: convert all to PDFs, then merge
        with tempfile.TemporaryDirectory() as temp_dir:
            pdf_paths = []
            for file_path in file_paths:
                ext = os.path.splitext(file_path)[1].lower()
                if ext in ['.jpg', '.jpeg', '.png']:
                    # For images, convert each to PDF
                    pdf_path = handle_conversion(file_path, output_folder=temp_dir, temp_dir=temp_dir)
                    if pdf_path:
                        pdf_paths.append(pdf_path)
                elif ext in ['.txt', '.docx', '.pdf', '.ppt', '.pptx']:
                    pdf_path = handle_conversion(file_path, output_folder=temp_dir, temp_dir=temp_dir)
                    if ext == '.docx':
                        # docx2pdf outputs as <filename>.pdf in temp_dir
                        pdf_path = os.path.join(temp_dir, os.path.splitext(os.path.basename(file_path))[0] + ".pdf")
                    if pdf_path and os.path.exists(pdf_path):
                        pdf_paths.append(pdf_path)
                else:
                    print(f"❌ Skipping unsupported file: {file_path}")

            if pdf_paths:
                output_pdf_path = os.path.join(output_folder, "combined_files.pdf")
                merge_pdfs(pdf_paths, output_pdf_path)
            else:
                print("❌ No files converted to PDF, nothing to merge.")

    print("🎉 All done! Converted files saved in:", output_folder)

if __name__ == "__main__":
    main()
