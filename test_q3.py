from count_people_mentions import CountPeopleMentions
from preprocess import Preprocess
import os
from utils import to_json_str, read_json_file_to_str, create_temp_file

def q3_test(sentences_content, people_content, remove_words_content, output_content) -> bool:
    try:
        sentences_path = create_temp_file(sentences_content)
        people_path = create_temp_file(people_content)
        remove_words_path = create_temp_file(remove_words_content)
        output_path = create_temp_file(output_content, ".json")

        preprocess_object = Preprocess(remove_words_path, sentences_path, people_path)
        people = CountPeopleMentions(preprocess_object.get_preprocessed_people(), preprocess_object.get_preprocessed_sentences()).task_3_format()
        actual_json_str = to_json_str(people)
        expected_json_str = read_json_file_to_str(output_path)
        return expected_json_str == actual_json_str
    except:
        return False
    finally:
        os.unlink(sentences_path)
        os.unlink(people_path)
        os.unlink(remove_words_path)
        os.unlink(output_path)

def test1():
    sentences_content = """sentence
"Under a tuft of jet- black hair over boy forehead Dumbledore and  McGonagall could see a curiously shaped cut, like a bolt of lightning."
` Is that where-?` whispered Professor  McGonagall.
"` Yes,` said  Dumbledore.`  Dumbledore'll have that scar forever.` ` Couldn't you do something about scar,  Dumbledore?` ` Even if I could, I wouldn't."
Scars can come in handy.
I have one myself above my left knee that is a perfect map of the London Underground.
"Well-- give  Dumbledore here,  Hagrid-- we'd better get this over with.`   Dumbledore took  Harry in  Harry arms and turned toward the   Mr. Dursley and   Mrs. Dursley and    Dudley Dursley' house."
"` Could I-- could I say good- bye to  Harry, sir?` asked  Hagrid."
"Harry bent  Harry great, shaggy head over  Harry and gave head what must have been a very scratchy, whiskery kiss."
"Then, suddenly,  Hagrid let out a howl like a wounded dog."
"` Shhh!` hissed Professor  McGonagall,` you'll wake the  Muggles!` ` S- s- sorry,` sobbed  Hagrid, taking out a large, spotted handkerchief and burying  Hagrid face in handkerchief.` But I c- c-can't stand handkerchief--  Lily an'  James dead-- an' poor little  Harry off ter live with  Muggles-` ` Yes, yes, handkerchief's all very sad, but get a grip on yourself,  Hagrid, or we'll be found,` Professor  McGonagall whispered, patting  Hagrid gingerly on the arm as  Dumbledore stepped over the low garden wall and walked to the front door."
"Dumbledore laid  Harry gently on the doorstep, took a letter out of  Dumbledore cloak, tucked letter inside  Harry's blankets, and then came back to the other two."
"For a full minute the three of two stood and looked at the little bundle;   Hagrid's shoulders shook, Professor  McGonagall blinked furiously, and the twinkling light that usually shone from  Dumbledore's eyes seemed to have gone out."
"` Well,` said  Dumbledore finally,` that's that."
We've no business staying here.
"We may as well go and join the celebrations.` ` Yeah,` said  Hagrid in a very muffled voice,` I'll be takin'  Sirius  Sirius bike back.G'night, Professor  McGonagall-- Professor  Dumbledore, sir.`  Wiping  Sirius streaming eyes on  Sirius jacket sleeve,  Hagrid swung  Hagrid onto the motorcycle and kicked the engine into life; with a roar engine rose into the air and off into the night."
"` I shall see you soon, I expect, Professor  McGonagall,` said  Dumbledore, nodding to voice."
Professor  McGonagall blew  McGonagall nose in reply.
Dumbledore turned and walked back down the street.
On the corner  Dumbledore stopped and took out the silver Put- Outer.
"Dumbledore clicked Outer once, and twelve balls of light sped back to balls street lamps so that Privet Drive glowed suddenly orange and  Dumbledore could make out a tabby cat slinking around the corner at the other end of the street."
Dumbledore could just see the bundle of blankets on the step of number four.
"` Good luck,  Harry,`  Dumbledore murmured."
"Dumbledore turned on  Dumbledore heel and with a swish of  Dumbledore cloak,  Dumbledore was gone."
"A breeze ruffled the neat hedges of Privet Drive, which lay silent and tidy under the inky sky, the very last place you would expect astonishing things to happen."
Harry  Potter rolled over inside  Dumbledore blankets without waking up.
"One small hand closed on the letter beside  Dumbledore and  Dumbledore slept on, not knowing  Dumbledore was special, not knowing  Dumbledore was famous, not knowing  Dumbledore would be woken in a few hours' time by   Mrs. Dursley's scream as   Mrs. Dursley opened the front door to put out the milk bottles, nor that  Dumbledore would spend the next few weeks being prodded and pinched by  Dumbledore cousin   Dudley...  Dumbledore couldn't know that at this very moment, people meeting in secret all over the country were holding up people glasses and saying in hushed voices:` To   Harry  Potter-- the boy who lived!"
"THE VANISHING GLASS  Nearly ten years had passed since the   Mr. Dursley and   Mrs. Dursley and    Dudley Dursley had woken up to find   Mr. Dursley and   Mrs. Dursley and    Dudley Dursley nephew on the front step, but Privet Drive had hardly changed at all."
"The sun rose on the same tidy front gardens and lit up the brass number four on the   Mr. Dursley and   Mrs. Dursley and    Dudley Dursley' front door; number crept into   Mr. Dursley and   Mrs. Dursley and    Dudley Dursley living room, which was almost exactly the same as it had been on the night when   Mr. Dursley had seen that fateful news report about the owls."
Only the photographs on the mantelpiece really showed how much time had passed.
"Ten years ago, there had been lots of pictures of what looked like a large pink beach ball wearing different- colored bonnets-- but    Dudley Dursley was no longer a baby, and now the photographs showed a large blond boy riding boy first bicycle, on a carousel at the fair, playing a computer game with boy father, being hugged and kissed by boy mother."
"The room held no sign at all that another boy lived in the house, too."
"""
    people_content = """Name,Other Names
Over-Attentive Wizard,
Bertram Aubrey,
Audrey Weasley,
"Augusta ""Gran"" Longbottom",
Augustus Pye,
Augustus Rookwood,
Augustus Worme,
Auntie Muriel,
Aunt Marge Dursley,
Aurelius Dumbledore,
Aurora Sinistra,
Avery,
Babajide Akingbade,
Babayaga,
Babbitty Rabbitty,
Bagman Sr.,
Ludo Bagman,
Otto Bagman,
Millicent Bagnold,
Bathilda Bagshot,batty
Kquewanda Bailey,
Ballyfumble Stranger,"quin, quivering quintus, quintusofthesillyname"
"""
    remove_words_content = """words
a
about
above
actual
after
again
against
all
alreadi
also
alway
am
amp
an
and
ani
anoth
any
anyth
are
around
as
at
aww
babi
back
be
becaus
because
bed
been
befor
before
being
below
between
birthday
bit
book
both
boy
but
by
call
can
cannot
cant
car
check
com
come
could
day
did
didn
dinner
do
doe
does
doesn
doing
don
done
dont
down
during
each
eat
end
even
ever
everyon
exam
famili
feel
few
final
find
first
follow
for
found
friday
from
further
game
get
girl
give
gone
gonna
got
gotta
guess
guy
had
hair
happen
has
have
haven
having
he
head
hear
her
here
hers
herself
hey
him
himself
his
home
hour
hous
how
http
i
if
im
in
into
is
isn
it
its
itself
job
just
keep
know
last
later
least
leav
let
life
listen
littl
live
look
lot
lunch
made
make
man
mani
may
mayb
me
mean
meet
might
mom
monday
month
more
morn
most
move
movi
much
must
my
myself
need
never
new
night
no
nor
not
noth
now
of
off
on
once
one
onli
only
or
other
ought
our
ours
ourselves
out
over
own
peopl
phone
pic
pictur
play
post
put
quot
rain
read
readi
realli
run
said
same
saw
say
school
see
seem
she
shop
should
show
sinc
sleep
so
some
someon
someth
song
soon
sound
start
stay
still
studi
stuff
such
summer
sunday
sure
take
talk
tell
than
thank
that
the
their
theirs
them
themselves
then
there
these
they
thing
think
this
those
though
thought
through
time
to
today
tomorrow
tonight
too
total
tri
tweet
twitpic
twitter
two
u
under
until
up
updat
use
veri
very
video
wait
wanna
want
was
watch
way
we
weather
week
weekend
went
were
what
when
where
whi
which
while
who
whom
why
will
with
woke
won
work
world
would
www
yay
yeah
year
yes
yesterday
yet
you
your
yours
yourself
yourselves
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
k
r
s
t
u
v
w
x
u
z
mr
miss
mrs
ms
"""
    output_content = """{
    "Question 3": {
        "Name Mentions": [
            [
                "aunt marge dursley",
                19
            ],
            [
                "aurelius dumbledore",
                32
            ]
        ]
    }
}"""

    assert q3_test(sentences_content, people_content, remove_words_content, output_content)

def test2():
    sentences_content = """sentence
"Karkaroff looked extremely worried, and  Snape looked angry."
Karkaroff hovered behind  Snape's desk for the rest of the double period.
Karkaroff seemed intent on preventing  Snape from slipping away at the end of class.
"Keen to hear what Karkaroff wanted to say,  Harry deliberately knocked over  Harry bottle of armadillo bile with two minutes to go to the bell, which gave  Harry an excuse to duck down behind  Harry cauldron and mop up while the rest of the class moved noisily toward the door."
` What's so urgent?`  Harry heard  Snape hiss at Karkaroff.
"` This,` said Karkaroff, and  Harry, peering around the edge of  Harry cauldron, saw Karkaroff  pull up the left- hand sleeve of  Harry robe and show  Snape something on  Harry inner forearm."
"` Well?` said Karkaroff, still making every effort not to move  Harry lips.` Do you see?"
the boy
"""
    people_content = """Name,Other Names
Ignatia Wildsmith,
Ignatius Prewett,
Ignatius Tuft,
Ignotus Peverell,
Igor Karkaroff,
Illyius,
Ingolfr the Iambic,
"""
    remove_words_content = """words
a
about
above
actual
after
again
against
all
alreadi
also
alway
am
amp
an
and
ani
anoth
any
anyth
are
around
as
at
aww
babi
back
be
becaus
because
bed
been
befor
before
being
below
between
birthday
bit
book
both
boy
but
by
call
can
cannot
cant
car
check
com
come
could
day
did
didn
dinner
do
doe
does
doesn
doing
don
done
dont
down
during
each
eat
end
even
ever
everyon
exam
famili
feel
few
final
find
first
follow
for
found
friday
from
further
game
get
girl
give
gone
gonna
got
gotta
guess
guy
had
hair
happen
has
have
haven
having
he
head
hear
her
here
hers
herself
hey
him
himself
his
home
hour
hous
how
http
i
if
im
in
into
is
isn
it
its
itself
job
just
keep
know
last
later
least
leav
let
life
listen
littl
live
look
lot
lunch
made
make
man
mani
may
mayb
me
mean
meet
might
mom
monday
month
more
morn
most
move
movi
much
must
my
myself
need
never
new
night
no
nor
not
noth
now
of
off
on
once
one
onli
only
or
other
ought
our
ours
ourselves
out
over
own
peopl
phone
pic
pictur
play
post
put
quot
rain
read
readi
realli
run
said
same
saw
say
school
see
seem
she
shop
should
show
sinc
sleep
so
some
someon
someth
song
soon
sound
start
stay
still
studi
stuff
such
summer
sunday
sure
take
talk
tell
than
thank
that
the
their
theirs
them
themselves
then
there
these
they
thing
think
this
those
though
thought
through
time
to
today
tomorrow
tonight
too
total
tri
tweet
twitpic
twitter
two
u
under
until
up
updat
use
veri
very
video
wait
wanna
want
was
watch
way
we
weather
week
weekend
went
were
what
when
where
whi
which
while
who
whom
why
will
with
woke
won
work
world
would
www
yay
yeah
year
yes
yesterday
yet
you
your
yours
yourself
yourselves
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
k
r
s
t
u
v
w
x
u
z
mr
miss
mrs
ms
"""
    output_content = """{
    "Question 3": {
        "Name Mentions": [
            [
                "igor karkaroff",
                8
            ]
        ]
    }
}"""

    assert q3_test(sentences_content, people_content, remove_words_content, output_content)


def test3():
    sentences_content = """sentence
"This is urgent,' said  Harry curtly.   '"
"Ooooh, urgent, is This?'"
said the other gargoyle in a high- pitched voice.'
"Well, that's put us in our place, hasn't that?'"
Harry knocked.
"Harry heard footsteps, then the door opened and  Harry found  Harry face to face with Professor  McGonagall.   '"
You haven't been given another detention!'
"McGonagall said at once,  McGonagall square spectacles flashing alarmingly.   '"
"""
    people_content = """Name,Other Names
"Magnus ""Dent Head"" Macdonald",
Magorian,
Maisie Cattermole,
Malcolm,
Malcolm Baddock,
Malcolm McGonagall,
Harold Skively,
Harper,
Harry Potter,"the boy who lived, undesirable number one, the chosen one, parry otter, the chosen boy, the mudbloods friend"
Harvey Ridgebit,
Hassan Mostafa,
"""
    remove_words_content = """words
a
about
above
actual
after
again
against
all
alreadi
also
alway
am
amp
an
and
ani
anoth
any
anyth
are
around
as
at
aww
babi
back
be
becaus
because
bed
been
befor
before
being
below
between
birthday
bit
book
both
boy
but
by
call
can
cannot
cant
car
check
com
come
could
day
did
didn
dinner
do
doe
does
doesn
doing
don
done
dont
down
during
each
eat
end
even
ever
everyon
exam
famili
feel
few
final
find
first
follow
for
found
friday
from
further
game
get
girl
give
gone
gonna
got
gotta
guess
guy
had
hair
happen
has
have
haven
having
he
head
hear
her
here
hers
herself
hey
him
himself
his
home
hour
hous
how
http
i
if
im
in
into
is
isn
it
its
itself
job
just
keep
know
last
later
least
leav
let
life
listen
littl
live
look
lot
lunch
made
make
man
mani
may
mayb
me
mean
meet
might
mom
monday
month
more
morn
most
move
movi
much
must
my
myself
need
never
new
night
no
nor
not
noth
now
of
off
on
once
one
onli
only
or
other
ought
our
ours
ourselves
out
over
own
peopl
phone
pic
pictur
play
post
put
quot
rain
read
readi
realli
run
said
same
saw
say
school
see
seem
she
shop
should
show
sinc
sleep
so
some
someon
someth
song
soon
sound
start
stay
still
studi
stuff
such
summer
sunday
sure
take
talk
tell
than
thank
that
the
their
theirs
them
themselves
then
there
these
they
thing
think
this
those
though
thought
through
time
to
today
tomorrow
tonight
too
total
tri
tweet
twitpic
twitter
two
u
under
until
up
updat
use
veri
very
video
wait
wanna
want
was
watch
way
we
weather
week
weekend
went
were
what
when
where
whi
which
while
who
whom
why
will
with
woke
won
work
world
would
www
yay
yeah
year
yes
yesterday
yet
you
your
yours
yourself
yourselves
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
k
r
s
t
u
v
w
x
u
z
mr
miss
mrs
ms
"""
    output_content = """{
    "Question 3": {
        "Name Mentions": [
            [
                "harry potter",
                5
            ],
            [
                "malcolm mcgonagall",
                3
            ]
        ]
    }
}"""

    assert q3_test(sentences_content, people_content, remove_words_content, output_content)

def test4():
    sentences_content = """sentence
"This is urgent,' said  Harry curtly.   '"
"Ooooh, urgent, is This?'"
said the other gargoyle in a high- pitched voice.'
"Well, that's put us in our place, hasn't that?'"
Harry knocked.
"Harry heard footsteps, then the door opened and  Harry found  Harry face to face with Professor  McGonagall.   '"
You haven't been given another detention!'
"McGonagall said at once,  McGonagall square spectacles flashing alarmingly.   '"
"""
    people_content = """Name,Other Names
Abernathy,
Abraham Peasegood,
Abraham Potter,
Abraxas Malfoy,
Achilles Tolliver,
Stewart Ackerley,
Mrs. Granger,
Hermione Granger,
Hugo Granger-Weasley,
Rose Granger-Weasley,
Granville Jorkins,
"""
    remove_words_content = """words
a
about
above
actual
after
again
against
all
alreadi
also
alway
am
amp
an
and
ani
anoth
any
anyth
are
around
as
at
aww
babi
back
be
becaus
because
bed
been
befor
before
being
below
between
birthday
bit
book
both
boy
but
by
call
can
cannot
cant
car
check
com
come
could
day
did
didn
dinner
do
doe
does
doesn
doing
don
done
dont
down
during
each
eat
end
even
ever
everyon
exam
famili
feel
few
final
find
first
follow
for
found
friday
from
further
game
get
girl
give
gone
gonna
got
gotta
guess
guy
had
hair
happen
has
have
haven
having
he
head
hear
her
here
hers
herself
hey
him
himself
his
home
hour
hous
how
http
i
if
im
in
into
is
isn
it
its
itself
job
just
keep
know
last
later
least
leav
let
life
listen
littl
live
look
lot
lunch
made
make
man
mani
may
mayb
me
mean
meet
might
mom
monday
month
more
morn
most
move
movi
much
must
my
myself
need
never
new
night
no
nor
not
noth
now
of
off
on
once
one
onli
only
or
other
ought
our
ours
ourselves
out
over
own
peopl
phone
pic
pictur
play
post
put
quot
rain
read
readi
realli
run
said
same
saw
say
school
see
seem
she
shop
should
show
sinc
sleep
so
some
someon
someth
song
soon
sound
start
stay
still
studi
stuff
such
summer
sunday
sure
take
talk
tell
than
thank
that
the
their
theirs
them
themselves
then
there
these
they
thing
think
this
those
though
thought
through
time
to
today
tomorrow
tonight
too
total
tri
tweet
twitpic
twitter
two
u
under
until
up
updat
use
veri
very
video
wait
wanna
want
was
watch
way
we
weather
week
weekend
went
were
what
when
where
whi
which
while
who
whom
why
will
with
woke
won
work
world
would
www
yay
yeah
year
yes
yesterday
yet
you
your
yours
yourself
yourselves
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
k
r
s
t
u
v
w
x
u
z
mr
miss
mrs
ms
"""
    output_content = """{
    "Question 3": {
        "Name Mentions": []
    }
}"""

    assert q3_test(sentences_content, people_content, remove_words_content, output_content)
