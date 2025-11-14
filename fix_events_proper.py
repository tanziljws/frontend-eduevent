#!/usr/bin/env python3
"""
Script untuk memperbaiki file Events.js dengan tepat
Fokus: Menambahkan loading state untuk banner
"""

def fix_events_file():
    # Baca file original
    with open('src/pages/Events_original.js', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Cari dan perbaiki bagian banner section
    fixed_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Cari baris yang berisi kondisi banner
        if '{banners.length > 0 ? (' in line and i > 500:
            # Ganti dengan kondisi yang benar (tambahkan loading state)
            indent = len(line) - len(line.lstrip())
            spaces = ' ' * indent
            
            # Tambahkan loading state
            fixed_lines.append(f'{spaces}{{bannersLoading ? (\n')
            fixed_lines.append(f'{spaces}  <div className="w-full h-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">\n')
            fixed_lines.append(f'{spaces}    <div className="text-white text-center">\n')
            fixed_lines.append(f'{spaces}      <div className="inline-block animate-spin rounded-full h-12 w-12 border-4 border-white border-t-transparent mb-4"></div>\n')
            fixed_lines.append(f'{spaces}      <p className="text-lg font-semibold">Memuat banner...</p>\n')
            fixed_lines.append(f'{spaces}    </div>\n')
            fixed_lines.append(f'{spaces}  </div>\n')
            fixed_lines.append(f'{spaces}) : banners.length > 0 ? (\n')
            i += 1
        # Skip duplikasi return statement
        elif line.strip().startswith('return (') and i > 400 and i < 500:
            # Cek apakah ini duplikasi
            # Cari return statement berikutnya
            found_duplicate = False
            for j in range(i+1, min(i+100, len(lines))):
                if lines[j].strip().startswith('return ('):
                    found_duplicate = True
                    break
            
            if found_duplicate:
                # Skip baris ini (duplikasi)
                i += 1
                continue
            else:
                fixed_lines.append(line)
                i += 1
        # Hapus tag AnimatePresence yang salah tempat (di dalam categories map)
        elif '</AnimatePresence>' in line and i > 500 and i < 550:
            # Cek apakah ini di dalam categories.map
            context_before = ''.join(lines[max(0, i-10):i])
            if 'categories.map' in context_before and '</li>' not in line:
                # Skip baris ini (tag yang salah tempat)
                # Tambahkan penutup yang benar
                indent = len(line) - len(line.lstrip())
                spaces = ' ' * indent
                fixed_lines.append(f'{spaces}  ))}}\n')
                fixed_lines.append(f'{spaces}</ul>\n')
                fixed_lines.append(f'{spaces[:-2]})</div>\n')
                fixed_lines.append(f'{spaces[:-4]}</div>\n')
                i += 1
            else:
                fixed_lines.append(line)
                i += 1
        else:
            fixed_lines.append(line)
            i += 1
    
    # Tulis file yang sudah diperbaiki
    with open('src/pages/Events.js', 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)
    
    print("✅ File Events.js berhasil diperbaiki!")
    print("📝 Perubahan:")
    print("   1. Menambahkan loading state untuk banner (bannersLoading)")
    print("   2. Menghapus duplikasi return statement")
    print("   3. Memperbaiki struktur JSX yang rusak")
    print("\n🔍 Silakan cek file dan test di browser!")

if __name__ == '__main__':
    fix_events_file()
