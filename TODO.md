PROJECTS

Short-term & Interesting
------------------------

	o Shared space is creating the same dictionary for different agents. it also doesn't get called from the activity_update because being at home doesn't have an activity. Need some lazy-state activity that comes in so that it is triggered while at home.
	o Positive and negative bonds form slowly by doing activities in the same space
	o Probability of a positive or negative micro-interaction is directly related to your current relationship
	o Clear out activities when completed
	o Social activities are based on feelings
	o dinner time needs to adjust to when people get home
	o Create more independent priorities
	    Plug in
	o Social priorities
	    Make love
	    Play with kids
	    Play with friends
	o Days of the week
	o Print logs in sensible, tabular format
	    Agent - role - going to do - location

Code quality & skills
---------------------

	o Create modules and import them
	o An occupation is a priority...and so is a priority
	o Is move a priority/activity?
    o Use parent and child classes
    o Priorities inherit a parent which includes activity_update
    o Make jobs less hacky when the agent is called. Find a way to use an argument to class conversion
    o Append simplicity
    o wtf are private vs. public functions? refresh on advanced programming. this will make a big difference. including style guides.
    o self isn't used in the commute logic
    o How do you create two separate instances of one variable gracefully (not a pointer)

Long-term
---------

    o Negative relationships form
    o Witnesses tell friends who tell other friends... information passes on
    o Different occupations
    o Visual representation
    o Spacial awareness & basic social interaction
    o Randomness
    o Hierarchy of needs. Defined by priority levels? General template, but personalized.
    o Create a larger world map of 3 houses, school, office, farm, restaurant/bar, park, gym
    o Planning behavior vs. habit. If no behavior exists, flip a coin? Could also be based on traits.
    o The impact that a behavior has on a witness' mood is tied to the intent, strength of the relationship, empathy with those in the situation, and level of independence of the witness. Associations change over time. Mood impacts underlying characteristics.
    o Data repeatedly observed becomes a belief
    o Lies
    o Create traits & moods that will influence behaviors
    o Traits change slowly over time, mood vary more widely
    o Meyers Brigg?
        Extrovert vs. Introvert - Impact social routine, family routine, encounters, and work style
        Judging vs. Perceiving - Structured vs. spontaneous
    o Moods
        Positive vs. negative - Happy increases quality/ speed of behavior, sad decreases it. Both can create new behaviors/ cancel behaviors.
        Energetic vs. relaxed
    o Economics
    o Triggers - Seeing something good or bad happen in your space impacts mood
    o Darkness: Sickness and death, depression, alcoholism, drugs, violence, crime
    o World is randomly generated
    o Model goes beyond a day
    o One-second increments
    o Agents have memory. Used for AI. Memory is not just what they experience personally but what they observe, including on TV.