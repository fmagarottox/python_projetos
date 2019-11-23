AGENDA = {
    'filipe': {
        'tel': '96474-1997',
        'e-mail': 'filipemagarottosc@gmail.com',
    },
    'ana': {
        'tel': '91234-5678',
        'e-mail': 'ana@gmail.com'
    }
}

AGENDA['lucas'] = {
    'tel': '91592-1840',
    'e-mail': 'lucas@gmail.com'
}

AGENDA['lucas']['tel'] = '99999-9999'

print(AGENDA['lucas']['tel'])