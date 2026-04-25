import sys

def patch():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Admin Icons (Editar y Eliminar)
    old_icons = '''                            <button @click.stop="editProduct(p)" class="p-2 bg-white/10 backdrop-blur-md rounded-2xl text-white hover:bg-gold-500 hover:text-black transition-all shadow-xl"><i data-lucide="edit-3" class="w-5 h-5"></i></button>
                            <button @click.stop="deleteProduct(p.id)" class="p-2 bg-white/10 backdrop-blur-md rounded-2xl text-white hover:bg-red-600 transition-all shadow-xl"><i data-lucide="trash-2" class="w-5 h-5"></i></button>'''
    
    new_icons = '''                            <button @click.stop="editProduct(p)" class="p-2 bg-gold-500 text-black backdrop-blur-md rounded-xl hover:scale-110 transition-transform shadow-xl"><i data-lucide="edit-3" class="w-5 h-5"></i></button>
                            <button @click.stop="deleteProduct(p.id)" class="p-2 bg-red-600 text-white backdrop-blur-md rounded-xl hover:scale-110 transition-transform shadow-xl"><i data-lucide="trash-2" class="w-5 h-5"></i></button>'''
    content = content.replace(old_icons, new_icons)
    
    # Ensure they don't use opacity-0 group-hover:opacity-100
    content = content.replace('absolute top-4 right-4 z-20 flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity', 'absolute top-4 right-4 z-20 flex gap-2')

    # 2. Border on editor inputs
    old_css = '''        .dashboard-input {
            background-color: #0c0c0c !important;
            color: #ffffff !important;
            @apply w-full border-2 border-white/80 rounded-2xl px-4 py-3 outline-none transition-all font-bold text-base;
            border-style: solid !important;
        }
        .dashboard-input:focus { @apply border-whatsapp bg-black !important; box-shadow: 0 0 25px rgba(37,211,102,0.3); }'''
    
    new_css = '''        .dashboard-input {
            background-color: #0c0c0c !important;
            color: #ffffff !important;
            border: 2px solid rgba(255, 255, 255, 0.4) !important;
            @apply w-full rounded-xl px-4 py-3 outline-none transition-all font-bold text-sm;
        }
        .dashboard-input:focus { 
            border-color: #fbbf24 !important; 
            box-shadow: 0 0 15px rgba(251, 191, 36, 0.3) !important; 
            background-color: #000000 !important;
        }'''
    content = content.replace(old_css, new_css)

    # 3. Image persistence (compress image on paste) and Save fix
    # Add the scrollTo top logic in init
    content = content.replace(
        'init() {',
        'init() {\\n                    window.scrollTo(0, 0);\\n                    history.replaceState(null, null, \\' \\');\\n'
    )
    
    # Replace save()
    old_save = "save() { localStorage.setItem('maru_vElite_Final_v4', JSON.stringify(this.products)); },"
    new_save = "save() { try { localStorage.setItem('maru_vElite_Final_v4', JSON.stringify(this.products)); } catch(e) { alert('Error: Espacio de almacenamiento lleno. Las imágenes deben ser más pequeñas o debes borrar productos.'); } },"
    content = content.replace(old_save, new_save)
    
    # Add compressImage method after save()
    compress_func = new_save + '''
                compressImage(base64, callback) {
                    const img = new Image();
                    img.src = base64;
                    img.onload = () => {
                        const canvas = document.createElement('canvas');
                        const MAX_WIDTH = 700;
                        let width = img.width;
                        let height = img.height;
                        if (width > MAX_WIDTH) { height = Math.round((height * MAX_WIDTH) / width); width = MAX_WIDTH; }
                        canvas.width = width; canvas.height = height;
                        const ctx = canvas.getContext('2d');
                        ctx.drawImage(img, 0, 0, width, height);
                        callback(canvas.toDataURL('image/jpeg', 0.6));
                    };
                },'''
                
    content = content.replace(new_save, compress_func)

    # Replace the paste listener with compressed logic
    old_paste = '''                                        const reader = new FileReader();
                                        reader.onload = (ev) => {
                                            this.form.images.push(ev.target.result);
                                            if (!this.form.mainImage) this.form.mainImage = ev.target.result;
                                            this.notify('Imagen añadida');
                                            setTimeout(() => isPasting = false, 500);
                                        };
                                        reader.readAsDataURL(items[i].getAsFile());'''
    new_paste = '''                                        const reader = new FileReader();
                                        reader.onload = (ev) => {
                                            this.compressImage(ev.target.result, (compressedUrl) => {
                                                this.form.images.push(compressedUrl);
                                                if (!this.form.mainImage) this.form.mainImage = compressedUrl;
                                                this.notify('Imagen añadida (Optimizada)');
                                                setTimeout(() => isPasting = false, 500);
                                            });
                                        };
                                        reader.readAsDataURL(items[i].getAsFile());'''
    content = content.replace(old_paste, new_paste)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

patch()
print("Patch applied successfully.")
