import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/sorna/Documents/germinare-supabase/data_hoje.json', encoding='utf-8') as f:
    d = json.load(f)

after_f1 = d['after_f1']
passed_f2 = ['Vanessa Germinare 🌱', 'Thais Camila', 'Fabricio', 'Leandro', 'Daiane Lemes', 'Giulliana Diniz']

chats_f2 = [c for c in after_f1 if c['chat'] in passed_f2]

for c in chats_f2:
    lines = []
    for m in c['mensagens']:
        txt = m.get('texto') or '[' + str(m.get('tipo','?')) + ']'
        lines.append(m['de'] + ' [' + m['hora'] + ']: ' + txt)
    transcript = '\n'.join(lines)
    safe_name = c['chat'].replace(' ', '_').replace('/', '_').replace('|', '').replace('🌱', 'leaf').replace('  ', '_')
    fname = 'C:/Users/sorna/Documents/germinare-supabase/tr2_' + safe_name + '.txt'
    with open(fname, 'w', encoding='utf-8') as fp:
        fp.write('CONVERSA: ' + c['chat'] + '\nDATA: 2026-05-12\nTOTAL: ' + str(c['total']) + ' msgs\n\n' + transcript)
    print('Saved:', fname, '(' + str(c['total']) + ' msgs)')
