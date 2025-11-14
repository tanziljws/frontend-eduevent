#!/usr/bin/env python3
"""
Script untuk memperbaiki file Events.js yang rusak
"""

def fix_events_file():
    # Baca file backup
    with open('src/pages/Events.js.backup', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hapus duplikasi return statement dan perbaiki struktur
    # Cari posisi duplikasi
    first_return = content.find('  return (', 400)
    second_return = content.find('\nreturn (', first_return + 10)
    
    if second_return > 0:
        # Hapus dari first_return sampai sebelum second_return
        content = content[:first_return] + content[second_return+1:]
    
    # Perbaiki bagian banner dengan menambahkan loading state
    # Cari bagian banner rendering
    banner_section_start = content.find('{banners.length > 0 ? (')
    if banner_section_start > 0:
        # Replace dengan kondisi yang benar
        old_condition = '{banners.length > 0 ? ('
        new_condition = '{bannersLoading ? (\n              <div className="w-full h-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">\n                <div className="text-white text-center">\n                  <div className="inline-block animate-spin rounded-full h-12 w-12 border-4 border-white border-t-transparent mb-4"></div>\n                  <p className="text-lg font-semibold">Memuat banner...</p>\n                </div>\n              </div>\n            ) : banners.length > 0 ? ('
        
        content = content.replace(old_condition, new_condition, 1)
    
    # Tulis file yang sudah diperbaiki
    with open('src/pages/Events.js', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ File Events.js berhasil diperbaiki!")
    print("📝 Perubahan:")
    print("   - Menghapus duplikasi return statement")
    print("   - Menambahkan loading state untuk banner")
    print("   - Memperbaiki struktur JSX")

if __name__ == '__main__':
    fix_events_file()
