# Finding DnaA Boxes
**Group 7: Alan Dayton, Cody Burt, Kaleb Olson**


---
## DnaA boxes in E. coli

Our first job was to locate the minimum skew which we found at the indices 3923620 to 3923623. This result confirms what is stated in the book.
Our next task was to run our frequent words algorithm to find 9-mers with a hamming distance of 1 over a window of some 500 bp. This however was met with less success as the most common 9-mers were not the ones listed in the textbook. We tried a few adjustments such as increasing the window to include 500 bp on each side of the minimum GC skew for a window of 1000 charaters, as well as increasing the distance of acceptible strings but again we did not find the same set of common kmers.

Later upon revewing the textbook an another attempt was made, this time with a 500bp window *starting* at the minimum GC skew instead of surrounding it. This time the desired string *was* in the set of common 9-mers; however, it was a suprise to see that size of the resulting set was 34! However, after consulting the textbook again, we saw that this mirrored what the book had indicated would happen.

After some further data munging which included removing reverse compliments from our results set and selecting only the matches that were exactly 1 hamming distance away. This yeilded a set that matched very closely what was in the textbook.

---
## DnaA boxes in mystery data

The exact same process was performed on the notSoSpooky data with varying parameters. The minimum GC skew was found to be near indices 3744269-3744271. The results yeilded a reasonably small set of possible 9-mers such that further wet lab testing could easily verify as being the DnaA binding box or not. For completeness we consider these 9-mers to likely to be either AGCTTCCGG, TGTGGATAA, or CCAGGATCC. Each result was fairly conclusive for each set of parameters used.

---
## Concluding remarks

In the future if such problems were to be attempted again we would likely plot a GC skew graph to visually confirm our window choice. 

Overall this analysis has underscored the importance of verifying our results in a lab. We saw that as valuable as bioformatic analysis is, it cannot tell us exact answers to some questions. For example we found many other 9-mers clustered near the minimum GC skew; any one of which could have potentially been the the DnaA binding box. However, when combined with traditional biological methods to verify the results the bioinformatic approach is invaluble when trying to make sense of biological data so as to focus research efforts.

