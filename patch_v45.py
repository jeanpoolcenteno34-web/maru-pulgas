import sys

file_path = r"c:\Users\jeanp\.gemini\antigravity\scratch\ventas-zapatillas\index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update version to 4.5
content = content.replace("v4.4", "v4.5")

# 2. Update Location texts
content = content.replace(
    '''<h2 class="text-4xl lg:text-5xl font-black font-display tracking-tighter uppercase leading-[0.85]">MARU PULGAS</h2>''',
    '''<h2 class="text-4xl lg:text-5xl font-black font-display tracking-tighter uppercase leading-[0.85]">MARU PULGAS - FERIA</h2>'''
)

content = content.replace(
    '''<p class="text-gold-500 font-bold text-base lg:text-lg tracking-tighter uppercase italic">Nuestro Showroom en La Molina</p>''',
    '''<p class="text-gold-500 font-bold text-base lg:text-lg tracking-tighter uppercase italic">Nuestra Feria en La Molina</p>'''
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied successfully.")
