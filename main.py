# SW 1
from pyscript import display, document

def check_student(e):
    document.getElementById('output').innerHTML = ''
    firstname = document.getElementById('first_name').value.strip()
    lastname = document.getElementById('last_name').value.strip()
    student_name = f"{firstname} {lastname }"
    club_members= ['Vita De Guzman', 'Destiny Reyes','MJ Madrelejos', 'Gurleen Kaur', 'Chalanie Lumbang', 'Julia Hadji Gapor', 'Kenneth Concepcion','Raver Estacio','Jesse Villante','Santiago Valdez', 'Miguel Jimenez']
    member_checker = student_name in club_members

    display_message = (f'Sorry, {student_name} you did not pass the auditions. You did not give any major gossip or chika.', f'Congratulations {student_name}, you are now part of the OBMC Gossip Club led by Franchesca Dela Rosa!')
    
    display(display_message[member_checker], target='output')


