# 🔍 DEBUG: BUTTON "BELI SEKARANG" TIDAK BISA DIKLIK

## Checklist Debug

Buka browser console (F12) dan jalankan commands berikut:

### 1. Check Environment Variable
```javascript
console.log('Client Key:', import.meta.env.VITE_MIDTRANS_CLIENT_KEY);
// Expected: "Mid-client-baNhlx1BONirl1UQ"
// If undefined: .env salah atau server belum di-restart
```

### 2. Check Snap Script Loaded
```javascript
console.log('Snap loaded:', typeof window.snap);
// Expected: "object"
// If "undefined": Script gagal load
```

### 3. Check Event Data
```javascript
// Di console, ketik:
document.querySelector('[class*="EventDetail"]')?.__reactFiber$?.return?.memoizedState
// Atau cek di React DevTools
```

### 4. Check Button Element
```javascript
const btn = document.querySelector('button:has-text("Beli Sekarang")');
console.log('Button:', btn);
console.log('Disabled:', btn?.disabled);
console.log('Pointer events:', window.getComputedStyle(btn)?.pointerEvents);
```

### 5. Check Network Tab
1. Open DevTools → Network
2. Reload page
3. Look for: `snap.js`
4. Status should be: **200 OK**

### 6. Check Console Errors
Look for any red errors in console, especially:
- CORS errors
- 404 errors
- Script loading errors
- React errors

## Common Issues

### Issue 1: Server Not Restarted
```bash
# Solution:
cd frontend-react.js
Ctrl + C
npm run dev
```

### Issue 2: Wrong Client Key Format
```env
# Check .env file
# Should start with: SB-Mid-client- (sandbox)
# Or: Mid-client- (production)
VITE_MIDTRANS_CLIENT_KEY=Mid-client-baNhlx1BONirl1UQ
```

### Issue 3: Event is Free
```javascript
// Check if event is actually paid
// In console:
console.log('Event is free:', event?.is_free);
console.log('Event price:', event?.price);
// If is_free = true, button will use Link instead of onClick
```

### Issue 4: User Not Logged In
```javascript
// Check if user is logged in
console.log('User:', user);
// If null, button will redirect to /login
```

### Issue 5: CSS Overlay
```javascript
// Check if there's an overlay blocking the button
const btn = document.querySelector('button:has-text("Beli Sekarang")');
const rect = btn?.getBoundingClientRect();
const elemAtPoint = document.elementFromPoint(rect.x + rect.width/2, rect.y + rect.height/2);
console.log('Element at button position:', elemAtPoint);
// Should be the button itself, not something else
```
