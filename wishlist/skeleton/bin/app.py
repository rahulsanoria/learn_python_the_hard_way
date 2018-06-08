import web

urls = (
	'/dream' , 'Index'
	)

app = web.application(urls , globals())

render = web.template.render('templates/', base = "layout")

class Index:
	
	def GET(self):
		return render.frame_design()

	def POST(self):
		form = web.input(h = None , c = None , b = None , t = None , p = None , r = None , job_age = None , age_house = None , age_car = None , age_bike = None , age_phone = None ,age_travelling = None , age_r = None )
		H = int(form.h)
		C = int(form.c)
		B = int(form.b)
		P = int(form.p)
		T = int(form.t)
		R = int(form.r)
		#TOTAL_COST = H + C + B + P + T + R  
		JOB_AGE = int(form.job_age)

		AGE_HOUSE = int(form.age_house)
		AGE_CAR = int(form.age_car)
		AGE_BIKE = int(form.age_bike)
		AGE_PHONE = int(form.age_phone)
		AGE_TRAVELLING = int(form.age_travelling)
		AGE_R = int(form.age_r)

		time = AGE_HOUSE - JOB_AGE
		tot_sal = H / (time * 12)

		time = AGE_CAR - JOB_AGE
		tot_sal = tot_sal + (C / (time * 12))

		time = AGE_BIKE - JOB_AGE
		tot_sal = tot_sal + (B / (time * 12))

		time = AGE_PHONE - JOB_AGE
		tot_sal = tot_sal + (P / (time * 12))

		time = AGE_TRAVELLING - JOB_AGE
		tot_sal = tot_sal + (T / (time * 12))

		time = AGE_R - JOB_AGE
		tot_sal = tot_sal + (R / (time * 12)) 


		return render.index(total_salary = tot_sal)

if __name__ == "__main__":
	app.run()		