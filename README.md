# Xtern Data Science Screen

The problem:

"While osXtern has a few highlighted features, the data science team is focusing all of its efforts on expanding osXte
rn’s feature set. As part of the Community Highlights feature, users agree to share their location with TechPointX and
any individuals they choose. In future iterations, TechPointX hopes that the Community Highlights data could be used to
do more.


In order to help identify what type of information could be surfaced in future iterations, you have been tasked with
reviewing the the sample data collected from recent user tests. In your research, highlight any conclusions you believe
the data can draw to help guide future development opportunities.

Your Task:

Review the test user data, and draw any conclusions you can from the data set. Your research and conclusions should be
submitted as a link to a github repository. It is encouraged that your repository hosts a Jupyter (formerly iPython)
notebook."

So, I wasn't sure quite what I supposed to do here, since:
    a) I don't know what kind of features the OS would want to focus on
    b) The location coordinates are not real
    c) There's not much data to work with anyways

Regardless I thought of two ways the data could still influence features:
    1) looking at what days people are most active
    2) looking at what locations each person is at the most

These are the conclusions I reached:
    a) There aren't any days which stand out to be more active than the others, so there's not really a feature I
       could propose based on that.
    b) Some users look like they tend to move around a lot more than others -- you can tell because their most common
       location coordinates are in the single digits. Vice versa applies to users who tend to be more stationary.
       Perhaps a feature could be developed on the OS that caters to how active or inactive a user is based on their
       common coordinate appearances.
