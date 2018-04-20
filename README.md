# Movie-Ticket-Booking-System

## Description :-

This is a movie ticket booking website.

On running the server you first go to the 'Home Page' of the site. There you shall have the option logging in to your account or see the movies currently running in different theatres.
	If you choose to Sign In you are re-directed to a Log-In page where you are supposed to enter you login credentials. If you do not have an account yet you must first register yourself. The link to the registration page is given in the Log In page. To Login you can use your username or email-id along with your password. Once you login you shall be redirected to the Movies page.
	If you choose to go to the Movies page you shall simple be redirected there.

The Movies page will display the movies currently availabe in theatres. You have the option of filtering them by Language or by their Rating. On selecting a movie you you will see the movie description popping out in which on clicking the poster of the movie you will reach that movie page.

Now on that movie page you can see everything about that movie like the theatres in which the movie is being displayed and the time slots of that movie in that theatre.Also you can see the theatre description and its type(big,medium,small) on that page. Here you can see the movie description and cast and also rate the movie if you are logged in at that moment.Now according to your convenience you can select a movie timing of your choice in any theatre you want and then you will be redirected to the actual booking page.

On the booking page select the seats out of the seats which are available (i.e which are not grey).Upon selecting the seats you can also see the estimated bill amount at the end of the page.You can also deselect the seats which you don't like by clicking on the selected seats again. After finalising your seats you can click on "Pay Now" button at the end of the page. The button will redirect you to the login page if you are not logged in , else you will be taken to the confirmation page. From that page you can again go to the Movies page or Home Page or directly Logout.



## Running of code :-

 - we will run our code through nginx
 - First of all we will test our uWSGI server using command =uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi=
 - Then we will create a myproject.sock using =uwsgi --ini myproject.ini=
 - Then we will start our server using =sudo service nginx start=
 - For restarting our server use =sudo service nginx restart=
 - Open firefox and run localhost with port 5000 to run our app
