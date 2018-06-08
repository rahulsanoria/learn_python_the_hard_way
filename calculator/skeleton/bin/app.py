import web

urls = (
	'/cal' , 'Index'
	)

app = web.application(urls, globals())

render = web.template.render('templates/', base= 'layout')

class Index:

	def GET(self):
		return render.frame_design()

	def POST(self):
 		form  = web.input(first_n  = None, second_n = None, add_s = None , sud_s = None , mul_s = None , div_s = None , mod_s = None) 
 		a = int(form.first_n)
 		b =  int(form.second_n)
 		
	 	if form.add_s:
	 		ans = a + b
	 	elif form.sub_s:	
	 		ans = a - b
	 	elif form.mul_s:	
	 		ans = a * b
	 	elif form.div_s:
	 		ans = a / b
	 	elif form.mod_s:
	 		ans = a % b

 		res = " ASNWER : %d" % float(ans)
 		#res = "\n SUM : %r ,\n SUBTRACTION : %r ,\n MULTIPLY : %r ,\n DIVISION : %r ,\n MODULUS : %r" % (add , sub , mul , div , mod )
 		return render.index(result = res)  

if __name__ == "__main__":
	app.run()					