from fastapi import FastAPI, status


app = FastAPI()
library = {
    "ten_thu_vien": "Thư viện Rikkei",
    "dia_chi": "123 Nguyễn Văn Cừ, Hà Nội",
    "gio_mo_cua": "08:00 - 21:00",
}


@app.get("/api/v1/library-info", status_code=status.HTTP_200_OK)
def check_health():
    return library
