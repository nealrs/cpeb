#!/usr/bin/python
# see readme for info & usage
# Copyright 2014, Neal Shyam

import eventbrite
import sendgrid
import os

ak = os.environ['ak']
su = os.environ['su']
sp = os.environ['sp']

# event & organizer parameters

uk = '1415998876128238792681'
eid = '14383737145'
o = {'first':'Taylor', 'last':'Swift', 'email':'foo@b.ar'}
u = 'http://ibmhadoop.challengepost.com'

def send(f, l, e, t, o, u):
  message = sendgrid.Mail()
  message.add_to(f+' '+l+' <'+e+'>')
  message.set_subject('One last thing before '+ t)
  message.set_html(ghtml(f,e,t,u))
  message.set_text(gtext(f,e,t,u))
  message.set_from(o['first']+' '+o['last']+' <'+o['email']+'>')
  status, msg = s.send(message)

def ghtml(f, e, t, u):
    html = "<p>Hey "+f+",</p><p>I want to share some important instructions for this weekend. We're using ChallengePost to showcase all your projects and support the judging.<p>You need to Register now and then Submit your projects before the deadline, both at this link:<p><a href='"+u+"'>"+u+"</a><p>Here's what you need to do:</p><ol><li>Have EVERY person on your team go to the link above and click \"Register for this hackathon.\" (It will require you create ChallengePost accounts, which is a quick process if you haven't yet done it.)</li><br><li>One person from each team will Enter a Submission (which is a button you'll see after you Register). Toward the bottom of the submission form, it will ask you to add your teammates' email addresses. Make sure you enter the same email addresses your teammates used to create their ChallengePost accounts.</li><br><li>Start early by entering what info you can on the submission form, and then save it as a draft. That way you won't be rushed toward the end. You'll be able to keep updating it until the deadline on Sunday!</li></ol>"
    return html

def gtext(f, e, t, u):
    text = "Hey " +f+ ",\nI want to share some important instructions for this weekend. We're using ChallengePost to showcase all your projects and support the judging.\nYou need to Register now and then Submit your projects before the deadline, both at this link:\n" +u+ "\nHere's what you need to do:\n1) Have EVERY person on your team go to the link above and click \"Register for this hackathon.\" (It will require you create ChallengePost accounts, which is a quick process if you haven't yet done it.)\n2) One person from each team will Enter a Submission (which is a button you'll see after you Register). Toward the bottom of the submission form, it will ask you to add your teammates' email addresses. Make sure you enter the same email addresses your teammates used to create their ChallengePost accounts.\n3) Start early by entering what info you can on the submission form, and then save it as a draft. That way you won't be rushed toward the end. You'll be able to keep updating it until the deadline on Sunday!"
    return text

### MAIN ###

# initialize event brite client & sendgrid
a = {'app_key':  ak, 'user_key': uk}
c = eventbrite.EventbriteClient(a)
e = c.event_get({'id':eid})
p = c.event_list_attendees({'id':eid})
s = sendgrid.SendGridClient(su, sp)

# get event title & email registrants
t = e['event']['title']
print "event title: " + t

for i in p['attendees']:
    x = i['attendee']
    f = x['first_name']
    l = x['last_name']
    e = x['email']

    # send email
    print "sending to..."+f+' '+l+' <'+e+'>'
    send(f, l, e, t, o, u)
