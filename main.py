from PyPDF2 import PdfReader


def read_pdf_in_chunks(file_path, pages_per_chunk=5):
    """
    Reads a PDF and yields text in fixed-size page windows.

    Args:
        file_path (str): Path to the PDF file.
        pages_per_chunk (int): Number of pages to return per chunk.

    Yields:
        tuple: (chunk_index, start_page, end_page, text)
    """
    reader = PdfReader(file_path)
    total_pages = len(reader.pages)

    for i in range(0, total_pages, pages_per_chunk):
        chunk_text = ""
        start_page = i + 1
        end_page = min(i + pages_per_chunk, total_pages)

        for j in range(i, end_page):
            page = reader.pages[j]
            chunk_text += page.extract_text() + "\n"

        yield (i // pages_per_chunk + 1, start_page, end_page, chunk_text.strip())


# Example usage
sum = 0
count = 0
if __name__ == "__main__":
    pdf_path = "harrypotter_1.pdf"

    for chunk_index, start, end, text in read_pdf_in_chunks(pdf_path):
        #print(f"\n📘 Chunk {chunk_index} (Pages {start}-{end})")
        sum += len(text)
        count += 1

    print(sum/count)