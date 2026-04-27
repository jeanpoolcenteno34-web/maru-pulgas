import sys

file_path = r"c:\Users\jeanp\.gemini\antigravity\scratch\ventas-zapatillas\index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update version to 5.0
content = content.replace("v4.5", "v5.0")

# 2. Update Location texts
content = content.replace(
    '''<p class="text-gold-500 font-bold text-base lg:text-lg tracking-tighter uppercase italic">Nuestra Feria en La Molina</p>''',
    '''<p class="text-gold-500 font-bold text-base lg:text-lg tracking-tighter uppercase italic">Nos encuentras en la Feria de La Molina</p>'''
)

# 3. Search Bar UI
content = content.replace(
    '''<div class="w-full lg:max-w-md relative">
                    <input type="text" x-model="search" autocomplete="off" placeholder="Buscar modelo..." class="w-full bg-white/5 border-4 border-white/10 rounded-full px-10 py-3 text-white font-bold outline-none focus:border-gold-500 transition-all text-base">
                    <i data-lucide="search" class="absolute left-4 top-1/2 -translate-y-1/2 text-white/20 w-5 h-5"></i>
                </div>''',
    '''<div class="w-full lg:max-w-2xl flex flex-col sm:flex-row gap-3 relative">
                    <div class="relative flex-1">
                        <input type="text" x-model="search" autocomplete="off" placeholder="Buscar modelo..." class="w-full h-full bg-white/5 border-4 border-white/10 rounded-full px-10 py-3 text-white font-bold outline-none focus:border-gold-500 transition-all text-base">
                        <i data-lucide="search" class="absolute left-4 top-1/2 -translate-y-1/2 text-white/20 w-5 h-5"></i>
                    </div>
                    <select x-model="sortOrder" class="bg-white/5 border-4 border-white/10 text-white/70 px-6 py-3 rounded-full outline-none focus:border-gold-500 transition-colors font-bold text-sm cursor-pointer hover:text-white appearance-none">
                        <option value="alpha" class="bg-premium-dark text-white">Orden Alfabético (A-Z)</option>
                        <option value="asc" class="bg-premium-dark text-white">Precio: Menor a Mayor</option>
                        <option value="desc" class="bg-premium-dark text-white">Precio: Mayor a Menor</option>
                    </select>
                </div>'''
)

# 4. Alpine State
content = content.replace(
    "products: [], search: '', brandFilter: 'ALL',",
    "products: [], search: '', sortOrder: 'alpha', brandFilter: 'ALL',"
)

# 5. Alpine Filter Logic
old_filter = "filteredProducts() { return this.products.filter(p => { const matchesSearch = (p.name || '').toLowerCase().includes(this.search.toLowerCase()); const matchesBrand = this.brandFilter === 'ALL' || (p.brand || '').toUpperCase() === this.brandFilter; return matchesSearch && matchesBrand; }); },"
new_filter = """filteredProducts() { 
                    let fp = this.products.filter(p => { 
                        const matchesSearch = (p.name || '').toLowerCase().includes(this.search.toLowerCase()); 
                        const matchesBrand = this.brandFilter === 'ALL' || (p.brand || '').toUpperCase() === this.brandFilter; 
                        return matchesSearch && matchesBrand; 
                    });
                    
                    if (this.sortOrder === 'alpha') {
                        fp.sort((a, b) => ((a.brand||'')+' '+(a.name||'')).localeCompare((b.brand||'')+' '+(b.name||'')));
                    } else if (this.sortOrder === 'asc') {
                        fp.sort((a, b) => {
                            const pa = parseFloat(a.offerPrice) || parseFloat(a.originalPrice) || 0;
                            const pb = parseFloat(b.offerPrice) || parseFloat(b.originalPrice) || 0;
                            return pa - pb;
                        });
                    } else if (this.sortOrder === 'desc') {
                        fp.sort((a, b) => {
                            const pa = parseFloat(a.offerPrice) || parseFloat(a.originalPrice) || 0;
                            const pb = parseFloat(b.offerPrice) || parseFloat(b.originalPrice) || 0;
                            return pb - pa;
                        });
                    }
                    return fp;
                },"""
content = content.replace(old_filter, new_filter)

# Double check that groupedProducts handles it well - yes, it maps over filteredProducts which are now sorted!
# However groupedProducts uses `groups[b].push(p)`. If they are already sorted by price, they will maintain that order within the group.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch v5 applied successfully.")
