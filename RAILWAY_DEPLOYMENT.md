# Railway Deployment Configuration

## Environment Variables

Untuk deploy frontend ke Railway, **WAJIB** set environment variable berikut di Railway dashboard:

### Required Environment Variable

```
REACT_APP_API_URL=https://your-backend-railway-url.up.railway.app/api
```

**Cara setup di Railway:**
1. Buka project **frontend** di Railway dashboard
2. Pilih tab **Variables** (atau **Settings** → **Variables**)
3. Klik **New Variable** atau **+ Add**
4. Tambahkan environment variable:
   - **Name:** `REACT_APP_API_URL`
   - **Value:** `https://your-backend-railway-url.up.railway.app/api`
     (Ganti `your-backend-railway-url` dengan URL backend Railway yang sebenarnya)
5. Klik **Add** untuk save
6. Trigger **Redeploy** untuk apply changes (biasanya otomatis setelah add variable)

⚠️ **PENTING:** Setelah menambahkan environment variable, aplikasi akan otomatis rebuild. Tunggu sampai deploy selesai.

### Default Value

Jika `REACT_APP_API_URL` **TIDAK** diset di Railway:
- ❌ Aplikasi akan default ke: `http://localhost:8000/api`
- ❌ Akan muncul error CORS: "Not allowed to request resource"
- ❌ API calls akan gagal karena mencoba connect ke localhost dari production

### For Local Development

Buat file `.env` di root folder `frontend-react.js/` (tidak akan di-commit ke git):

```
REACT_APP_API_URL=http://localhost:8000/api
```

Atau bisa menggunakan `.env.local`:

```
REACT_APP_API_URL=http://127.0.0.1:8000/api
```

## Cara Cek Backend URL di Railway

1. Buka backend project di Railway
2. Buka tab **Settings** → **Networking**
3. Copy **Public Domain** URL
4. Tambahkan `/api` di akhir URL

Contoh:
- Public Domain: `https://backend-eduevent-production.up.railway.app`
- API URL: `https://backend-eduevent-production.up.railway.app/api`

## Troubleshooting

### Error: "Origin is not allowed by Access-Control-Allow-Origin"
✅ **SOLVED** - Backend sudah dikonfigurasi untuk allow Railway frontend origin.

### Error: 404 Not Found pada `/banners` atau `/events`
❌ **Masalah:** Frontend masih menggunakan URL tanpa `/api` prefix atau environment variable belum diset.

**Solusi:**
1. Pastikan `REACT_APP_API_URL` di Railway frontend project menggunakan format: `https://backend-url.railway.app/api` (harus ada `/api` di akhir)
2. Contoh yang **BENAR:**
   ```
   REACT_APP_API_URL=https://backend-eduevent-production.up.railway.app/api
   ```
3. Contoh yang **SALAH:**
   ```
   REACT_APP_API_URL=https://backend-eduevent-production.up.railway.app
   ```
   (Tidak ada `/api` - akan menyebabkan 404 error)

4. Setelah update environment variable, trigger **Redeploy** di Railway
5. Tunggu deploy selesai (biasanya 2-5 menit)

### Error: "Network Error" atau "No response received"
- Pastikan backend Railway sudah running (cek health endpoint: `https://backend-url.railway.app/up`)
- Pastikan frontend URL di backend CORS config sudah benar (sudah dikonfigurasi di `config/cors.php`)

## Verification

Setelah deploy, cek browser console untuk memastikan:
- ✅ Tidak ada error "Not allowed to request resource"
- ✅ Tidak ada error "XMLHttpRequest cannot load http://localhost:8000"
- ✅ Tidak ada 404 error pada `/api/banners` atau `/api/events`
- ✅ API calls menggunakan URL Railway backend yang benar (dengan `/api` prefix)
- ✅ Request URL format: `https://backend-url.railway.app/api/events` ✅
- ❌ **BUKAN:** `https://backend-url.railway.app/events` ❌

## Quick Checklist

- [ ] `REACT_APP_API_URL` sudah diset di Railway frontend project
- [ ] URL format: `https://backend-url.railway.app/api` (dengan `/api`)
- [ ] Frontend sudah di-redeploy setelah set environment variable
- [ ] Backend sudah di-deploy dengan CORS config terbaru
- [ ] Cek browser console untuk verifikasi (tidak ada error)

