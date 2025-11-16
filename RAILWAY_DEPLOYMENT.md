# Railway Deployment Configuration

## Environment Variables

Untuk deploy frontend ke Railway, pastikan set environment variable berikut di Railway dashboard:

### Required Environment Variable

```
REACT_APP_API_URL=https://your-backend-railway-url.up.railway.app/api
```

**Cara setup di Railway:**
1. Buka project frontend di Railway dashboard
2. Pilih tab **Variables**
3. Tambahkan environment variable:
   - **Name:** `REACT_APP_API_URL`
   - **Value:** `https://your-backend-railway-url.up.railway.app/api`
     (Ganti `your-backend-railway-url` dengan URL backend Railway yang sebenarnya)

4. Setelah ditambahkan, trigger redeploy untuk apply changes

### Default Value

Jika `REACT_APP_API_URL` tidak diset, aplikasi akan default ke:
- Development: `http://localhost:8000/api`
- Production: akan error karena mencoba connect ke localhost

## Cara Cek Backend URL di Railway

1. Buka backend project di Railway
2. Buka tab **Settings** → **Networking**
3. Copy **Public Domain** URL
4. Tambahkan `/api` di akhir URL

Contoh:
- Public Domain: `https://backend-eduevent-production.up.railway.app`
- API URL: `https://backend-eduevent-production.up.railway.app/api`

## Verification

Setelah deploy, cek browser console untuk memastikan:
- ✅ Tidak ada error "Not allowed to request resource"
- ✅ Tidak ada error "XMLHttpRequest cannot load http://localhost:8000"
- ✅ API calls menggunakan URL Railway backend yang benar

