# Finding DnaA Boxes
**Group 7: Alan Dayton, Cody Burt, Kaleb Olson**


---
## DnaA boxes in E. coli

Our first job was to locate the minimum skew which we found at the indices 3923620 to 3923623. This result confirms what is stated in the book.
Our next task was to run our frequent words algorithm to find 9-mers with a hamming distance of 1 over a window of some 500 bp. We started with that window centered at the minimum GC skew, but the most common 9-mers we found were not the ones listed in the textbook. We tried a few adjustments, such as increasing the window to include 500 bp on each side of the minimum GC skew for a window of 1000 characters, as well as increasing the distance of acceptable strings but again we did not find the same set of common kmers.

Later upon reviewing the textbook an another attempt was made, this time with a 500bp window *starting* at the minimum GC skew instead of surrounding it. This time the desired string *was* in the set of common 9-mers; however, it was a surprise to see that size of the resulting set was 34! However, after consulting the textbook again, we saw that this mirrored what the book indicated would happen.

After some further data munging, which included removing reverse compliments from our results set and selecting only the matches that were exactly 1 hamming distance away, we found a set of 9-mers that matched very closely what was in the textbook. These 9-mers were TCTGGATAA, TGTGAATAA, TGTGGATAA and their reverse compliments.

---
## DnaA boxes in mystery data

The exact same process was performed on the notSoSpooky data with varying parameters. The minimum GC skew was found to be near indices 3744269-3744271. We tried windows centered at the miminum skew and starting at the minimum skew. The results yielded a reasonably small set of possible 9-mers such that further wet lab testing could easily verify as being the DnaA binding box or not. For completeness we consider these 9-mers to likely to be either AGCTTCCGG, TGTGGATAA, or CCAGGATCC. From these 9-mers, we suggest a reasonable range that could include the origin of replication is [   ,  ]. For each set of parameters (i.e. window size, window location) each result set was fairly conclusive. Since different sets of parameters yielded similar results, we are fairly confident with our prediction for the location of the origin of replication.

---
## Concluding remarks

In the future if such problems were to be attempted again we would likely plot a GC skew graph to visually confirm our window choice. 

Overall, this analysis has underscored the importance of verifying our results in a lab. We saw that as valuable as bioformatic analysis is, it cannot tell us exact answers to some questions. For example, we found many other 9-mers clustered near the minimum GC skew, any one of which could have potentially been the DnaA binding box. We had to adjust our algorithms to find results that matched the experimental results. With those adjusted algorithms, we were able to predict several possible DnaA boxes for the genome corresponding to the mystery organism. However, those results need to be checked against experimental data to determine which (if any) of the generated 9-mers are the actual DnaA boxes.

We can see that bioinformatic analysis must be accompanied by lab testing, but lab testing also relies heavily on bioinformatic analysis. Without computer algorithms to determine the minimum skew and predict DnaA boxes, scientists would have to check the whole genome to find the origin of replication, which would be a lengthy and tedious process. Bioinformatic analysis can reduce that search space to make the experimental validation a tractible problem.
