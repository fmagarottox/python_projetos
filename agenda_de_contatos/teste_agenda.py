AGENDA = {}

AGENDA['filipe'] = {
	'telefone': '96474-1997',
	'email': 'filipemagarotto@gmail.com',
	'endereco': 'Rua Tiradentes'
}

def mostrar_agenda():
	for contato in AGENDA:
		buscar_contato(contato)
		print('-------------------')

def buscar_contato(contato):
	print('Nome:', contato)
	print('Telefone:', AGENDA[contato]['telefone'])
	print('E-mail:', AGENDA[contato]['email'])
	print('Endereço:', AGENDA[contato]['endereco'])

def incluir_editar_contato(contato, telefone, email, endereco):
	AGENDA[contato] = {
		'telefone': telefone,
		'email': email,
		'endereco': endereco
	}
	print("Contato {} adicionado/editado com sucesso.".format(contato))

def excluir_contato(contato):
	AGENDA.pop(contato)
	print('contato excluido com sucesso.')

excluir_contato('filipe')
mostrar_agenda()
