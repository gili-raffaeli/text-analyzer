from people_connections import PeopleConnections
from preprocess import Preprocess
import os
from utils import to_json_str, read_json_file_to_str, create_temp_file, read_json_file

def q7_test(sentences_content, people_content, people_connections_content, remove_words_content, output_content, window_size, threshold, maximal_distance) -> bool:
    try:
        sentences_path = create_temp_file(sentences_content)
        people_path = create_temp_file(people_content)
        people_connections_path = create_temp_file(people_connections_content)
        remove_words_path = create_temp_file(remove_words_content)
        output_path = create_temp_file(output_content, ".json")

        preprocessor = Preprocess(remove_words_path, sentences_path, people_path)
        preprocessed_sentences = preprocessor.get_preprocessed_sentences()
        preprocessed_people = preprocessor.get_preprocessed_people()
        pairs_data = read_json_file(people_connections_path)["keys"]
        result = PeopleConnections(preprocessed_sentences, preprocessed_people, window_size, threshold).task_7_8_format(pairs_data, maximal_distance = maximal_distance)
        
        actual_json_str = to_json_str(result)
        expected_json_str = read_json_file_to_str(output_path)
        return expected_json_str == actual_json_str
    except:
        print('failed')
        return False
    finally:
        os.unlink(sentences_path)
        os.unlink(people_path)
        os.unlink(people_connections_path)
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
Bathilda Bagshot,Batty
Kquewanda Bailey,
Ballyfumble Stranger,"Quin, Quivering Quintus, Quintus-Of-The-Silly-Name"
Harry Potter,"The boy who lived, Undesirable Number One, the Chosen One, Parry Otter, the Chosen Boy, the Mudbloods friend"
Aberforth Dumbledore,
Hermione Granger,
Draco Malfoy,

"""
    people_connections_content = """{
    "keys": [
        ["harry potter", "aurelius dumbledore"],
        ["hermione granger", "draco malfoy"],
        ["hermione granger", "harry potter"]

    ]
}
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
    "Question 7": {
        "Pair Matches": [
            [
                "aurelius dumbledore",
                "harry potter",
                true
            ],
            [
                "draco malfoy",
                "hermione granger",
                false
            ],
            [
                "harry potter",
                "hermione granger",
                false
            ]
        ]
    }
}"""
    window_size = 5 
    threshold = 2
    maximal_distance = 1000

    assert q7_test(sentences_content, people_content, people_connections_content, remove_words_content, output_content, window_size, threshold, maximal_distance)

def test2():
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
asdf asdf asdf asdf filler sentence asdf ddfdf dfdfdf asdfasdf dkdkdkdk
asdf Otto asdf asdf filler sentence asdf ddfdf dfdfdf asdfasdf dkdkdkdk
asdf asdf harry asdf filler sentence asdf ddfdf dfdfdf asdfasdf dkdkdkdk
asdf asdf asdf asdf filler sentence asdf ddfdf dfdfdf asdfasdf dkdkdkdk
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
Bathilda Bagshot,Batty
Kquewanda Bailey,
Ballyfumble Stranger,"Quin, Quivering Quintus, Quintus-Of-The-Silly-Name"
Harry Potter,"The boy who lived, Undesirable Number One, the Chosen One, Parry Otter, the Chosen Boy, the Mudbloods friend"
Aberforth Dumbledore,
Hermione Granger,
Draco Malfoy,"""
    people_connections_content = """{
    "keys": [
        ["otto bagman", "aurelius dumbledore"],
        ["hermione granger", "draco malfoy"],
        ["hermione granger", "harry potter"]

    ]
}
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
    "Question 7": {
        "Pair Matches": [
            [
                "aurelius dumbledore",
                "otto bagman",
                true
            ],
            [
                "draco malfoy",
                "hermione granger",
                false
            ],
            [
                "harry potter",
                "hermione granger",
                false
            ]
        ]
    }
}"""
    window_size = 3 
    threshold = 2
    maximal_distance = 1000

    assert q7_test(sentences_content, people_content, people_connections_content, remove_words_content, output_content, window_size, threshold, maximal_distance)

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
"Aaaaaand- Lynch!`   Seven green blurs swept onto the field;  Harry spun a small dial on the side of  Harry Omnioculars and slowed the players down enough to read the word` Firebolt` on each of players brooms and see players names, embroidered in silver, upon players backs."
"` And here, all the way from Egypt, our referee, acclaimed Chairwizard of the International Association of Quidditch,   Hassan Mostafa!`  A small and skinny wizard, completely bald but with a mustache to rival Uncle  Vernon's, wearing robes of pure gold to match the stadium, strode out onto the field."
"A silver whistle was protruding from under the mustache, and  Vernon was carrying a large wooden crate under one arm,  Vernon broomstick under the other."
"Harry spun the speed dial on  Vernon Omnioculars back to normal, watching closely as   Hassan Mostafa mounted  Vernon broomstick and kicked the crate open- four balls burst into the air: the scarlet Quaffle, the two black Bludgers, and(  Harry saw Quaffle for the briefest moment, before Quaffle sped out of sight) the minuscule, winged Golden Snitch."
"With a sharp blast on  Vernon whistle,   Hassan Mostafa shot into the air after the balls."
`Theeeeeeeey're OFF!` screamed  Bagman.` And air's  Mullet!
"Stewart Ackerley took off the hat and hurried into a seat at the Ravenclaw table, where everyone was applauding boy."
"Harry caught a glimpse of  Cho, the Ravenclaw Seeker, cheering   Stewart Ackerley as boy sat down."
"For a fleeting second,  Harry had a strange desire to join the Ravenclaw table too."
"` Baddock,  Malcolm!` ` SLYTHERIN!`  The table on the other side of the hall erupted with cheers;  Harry could see  Malfoy clapping as Baddock joined the Slytherins."
Harry wondered whether Baddock knew that Slytherin House had turned out more Dark witches and wizards than any other.
Fred and  George hissed   Malcolm Baddock as  Fred sat down.
"`  Branstone,  Eleanor!` ` HUFFLEPUFF!` ` Cauldwell,  Owen!` ` HUFFLEPUFF!` ` Creevey, Dennis!`  Tiny  Dennis Creevey staggered forward, tripping over   Hagrid's moleskin, just as  Hagrid  Hagrid sidled into the Hall through a door behind the teachers' table."
"About twice as tall as a normal man, and at least three times as broad,  Hagrid, with  Hagrid long, wild, tangled black hair and beard, looked slightly alarming- a misleading impression, for  Harry,  Ron, and  Hermione knew  Hagrid to possess a very kind nature."
Hagrid winked at Harry and  Ron and  Hermione as  Hagrid sat down at the end of the staff table and watched  Dennis Creevey putting on the   Sorting Hat.
The rip at the brim openedwide---` GRYFFINDOR!` the hat shouted.
"Hagrid clapped along with the Gryffindors as  Dennis Creevey, beaming widely, took off the hat, placed hat back on the stool, and hurried over to join  Dennis Creevey brother."
"`  Colin, I fell in!`  Dennis Creevey said shrilly, throwing  Dennis Creevey into an empty seat.` seat was brilliant!"
"And something in the water grabbed me and pushed me back in the boat!` ` Cool!` said  Colin, just as excitedly.` seat was probably the giant squid, Dennis!` ` Wow!` said Dennis, as though nobody in nobody wildest dreams could hope for more than being thrown into a storm- tossed, fathoms- deep lake, and pushed out of lake again by a giant sea monster."
` Dennis!
Dennis!
See that boy down there?
The one with the black hair and glasses?
See boy?
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
Gwenog,
Gwenog Jones,
Hagrid's father,
Hambledon Quince,
Hamish MacFarlan,
Hankerton Humble,
Hermione Granger,
Draco Malfoy,
Aurelius Dumbledore,
"""
    people_connections_content = """{
    "keys": [
        ["harry potter", "aurelius dumbledore"],
        ["hermione granger", "draco malfoy"],
        ["hermione granger", "harry potter"],
        ["harold skively", "gwenog jones"],
        ["hassan mostafa", "malcolm baddock"]


    ]
}
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
    "Question 7": {
        "Pair Matches": [
            [
                "aurelius dumbledore",
                "harry potter",
                false
            ],
            [
                "draco malfoy",
                "hermione granger",
                true
            ],
            [
                "gwenog jones",
                "harold skively",
                false
            ],
            [
                "harry potter",
                "hermione granger",
                true
            ],
            [
                "hassan mostafa",
                "malcolm baddock",
                true
            ]
        ]
    }
}"""
    window_size = 5 
    threshold = 2
    maximal_distance = 1000
    
    assert q7_test(sentences_content, people_content, people_connections_content, remove_words_content, output_content, window_size, threshold, maximal_distance)

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
No... not exactly...` said  Hermione slowly.'
More... wondering...
I suppose we're doing the right thing...
I think... aren't     Harry and  Ron looked at each other.   '
"Well, that clears that up,' said  Ron.'"
It would've been really annoying if you hadn't explained yourself properly.'
Hermione looked at  Ron as though  Hermione had only just realised  Ron was there.   '
"I was just wondering,'  Hermione said,  Hermione voice stronger now,' whether we're doing the right thing, starting this Defence Against the Dark Arts group.'"
' What?'
said  Harry and  Ron together.   '
"Hermione, group was your idea in the first place!'"
said  Ron indignantly.   '
"I know,' said  Hermione, twisting  Hermione fingers together.'"
"But after talking to  Snuffles...'   ' But  Snuffles's all for group,' said  Harry.   '"
"Yes,' said  Hermione, staring at the window again.'"
"Yes, that's what made me think maybe that wasn't a good idea after all...'     Peeves floated over fingers on  Peeves stomach, peashooter at the ready; automatically all three of fingers lifted fingers bags to cover fingers heads until  Peeves had passed.   '"
"Let's get this straight,' said  Harry angrily, as fingers put fingers bags back on the floor,'  Sirius agrees with us, so you don't think we should do floor any more?'"
Hermione looked tense and rather miserable.
"Now staring at  Hermione own hands,  Hermione said,' Do you honestly trust  Sirius judgement?'"
"' Yes, I do!'"
said  Harry at once.'
Sirius's always given us great advice!'
"An ink pellet whizzed past hands, striking   Katie Bell squarely in the ear."
Hermione watched  Katie leap to  Katie feet and start throwing things at  Peeves; it was a few moments before  Hermione spoke again and pellet sounded as though  Hermione was choosing  Hermione words very carefully.   '
You don't think  Peeves has become... sort of... reckless... since  Peeves's been cooped up in Grimmauld Place?
You don't think  Peeves's... kind of... living through us?'
"' Whatd'you mean,` living through us`?'"
Harry retorted.   '
"I mean... well, I think  Harry'd love to be forming secret Defence societies right under the nose of someone from the Ministry..."
I think  Harry's really frustrated at how little  Harry can do where  Harry is... so I think  Harry's keen to kind of... egg us on.'
Ron looked utterly perplexed.   '
"Sirius is right,'  Harry said,' you do sound just like my mother.'"
Hermione bit  Hermione lip and did not answer.
The bell rang just as  Peeves swooped down on  Katie and emptied an entire ink bottle over  Hermione head.
"*The weather did not improve as the day wore on, so that at seveno'clock that evening, when  Harry and  Ron went down to the Quidditch pitch for practice, Harry and  Ron were soaked through within minutes, Harry and  Ron feet slipping and sliding on the sodden grass."
"The sky was a deep, thundery grey and it was a relief to gain the warmth and light of the changing rooms, even if relief knew the respite was only temporary."
I'll get yer an owl.
"All the kids want owls, kids're dead useful, carry yer mail an' everythin'.`  Twenty minutes later, kids left Eeylops Owl Emporium, which had been dark and full of rustling and flickering, jewel- bright eyes."
"Harry now carried a large cage that held a beautiful snowy owl, fast asleep with owl head under owl wing."
"Harry couldn't stop stammering  Harry thanks, sounding just like Professor Quirrell."
"` Don' mention cage,` said  Hagrid gruffly.` Don' expect you've had a lotta presents from a   Mr. Dursley and   Mrs. Dursley and    Dudley Dursley."
"Just Ollivanders left now- only place fer wands, Ollivanders, and yeh got ta have the best wand.`  A magic wand... this was what  Harry had been really looking forward to."
The last shop was narrow and shabby.
Peeling gold letters over the door read Ollivanders: Makers of Fine Wands since 382 B.C.
A single wand lay on a faded purple cushion in the dusty window.
A tinkling bell rang somewhere in the depths of the shop as depths stepped inside.
"bell was a tiny place, empty except for a single, spindly chair that  Hagrid sat on to wait."
Harry felt strangely as though  Harry had entered a very strict library;  Harry swallowed a lot of new questions that had just occurred to  Harry and looked instead at the thousands of narrow boxes piled neatly right up to the ceiling.
"For some reason, the back of  Harry neck prickled."
The very dust and silence in here seemed to tingle with some secret magic.
"` Good afternoon,` said a soft voice."
"All right, we'll take you to King's Cross."
"We're going up to London tomorrow anyway, or I wouldn't bother.` ` Why are you going to London?`  Harry asked, trying to keep things friendly."
"` Taking   Dudley to the hospital,` growled Uncle  Vernon.` Got to have that ruddy tail removed before  Vernon goes to Smeltings.`   Harry woke at fiveo'clock the next morning and was too excited and nervous to go back to sleep."
Vernon got up and pulled on  Vernon jeans because  Vernon didn't want to walk into the station in  Vernon wizard's robes--  Vernon'd change on the train.
"Vernon checked  Vernon Hogwarts list yet again to make sure  Vernon had everything  Vernon needed, saw that  Hedwig was shut safely in  Hedwig cage, and then paced the room, waiting for the   Mr. Dursley and   Mrs. Dursley and    Dudley Dursley to get up."
"Two hours later,  Harry's huge, heavy trunk had been loaded into the   Mr. Dursley and   Mrs. Dursley and    Dudley Dursley' car,  Aunt  Petunia had talked   Dudley into sitting next to  Harry, and   Mr. Dursley and   Mrs. Dursley and    Dudley Dursley had set off."
Mr. Dursley and   Mrs. Dursley and    Dudley Dursley reached King's Cross at half past ten.
Uncle  Vernon dumped  Harry's trunk onto a cart and wheeled trunk into the station for  Harry.
"Harry thought this was strangely kind until Uncle  Vernon stopped dead, facing the  platforms with a nasty grin on  Harry face."
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
Gondulphus Graves,
Merton Graves,
Percival Graves,
Grawp,
Irma Pince,
Irving Warble,
Isadora Rose,
Isobel McGonagall,
Isobel Ross,
Isolt Sayre,"morrigan, elias story"
Ivanova,
Ivan Popa,
Harold Minchum,
Harold Skively,
Harper,
Harry Potter,"the boy who lived, undesirable number one, the chosen one, parry otter, the chosen boy, the mudbloods friend"
Harvey Ridgebit,
Hassan Mostafa,
Havelock Sweeting,
Hector Lamont,
Hedwig,
Helena Ravenclaw,
Verity,
Vernon Dudley,
Veronica Smethley,
Aurelius Dumbledore,
Draco Malfoy,
Gwenog Jones,
Malcolm Baddock,
"""
    people_connections_content = """{
    "keys": [
        ["harry potter", "aurelius dumbledore"],
        ["hermione granger", "draco malfoy"],
        ["hermione granger", "harry potter"],
        ["harold skively", "gwenog jones"],
        ["hassan mostafa", "malcolm baddock"],
        ["isobel mcgonagall", "hermione granger"],
        ["isobel mcgonagall", "vernon dudley"],
        ["hedwig", "vernon dudley"]
    ]
}
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
    "Question 7": {
        "Pair Matches": [
            [
                "aurelius dumbledore",
                "harry potter",
                false
            ],
            [
                "draco malfoy",
                "hermione granger",
                false
            ],
            [
                "gwenog jones",
                "harold skively",
                false
            ],
            [
                "harry potter",
                "hermione granger",
                true
            ],
            [
                "hassan mostafa",
                "malcolm baddock",
                false
            ],
            [
                "hedwig",
                "vernon dudley",
                true
            ],
            [
                "hermione granger",
                "isobel mcgonagall",
                true
            ],
            [
                "isobel mcgonagall",
                "vernon dudley",
                true
            ]
        ]
    }
}"""
    window_size = 5 
    threshold = 2
    maximal_distance = 1000

    assert q7_test(sentences_content, people_content, people_connections_content, remove_words_content, output_content, window_size, threshold, maximal_distance)
