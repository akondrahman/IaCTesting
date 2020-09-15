Dear authors,


we are glad to inform you that your paper Testing Practices for Infrastructure as Code has been accepted to LANGETI'20

Please note that the camera ready version of the paper is on September 17. This deadline was imposed by the publisher and is strict

SUBMISSION: 2
TITLE: Testing Practices for Infrastructure as Code


----------------------- REVIEW 1 ---------------------
SUBMISSION: 2
TITLE: Testing Practices for Infrastructure as Code
AUTHORS: Mohammed Mehedi Hasan, Farzana Ahamed Bhuiyan and Akond Rahman

----------- Overall evaluation -----------
SCORE: 1 (weak accept)
----- TEXT:
Summary:
The authors review the state-of-practice regarding testing of Infrastructure-As-Code (IaC) artefacts. To gather them, they review grey literature identifying six key practices.

Pros:
It explores a highly relevant subject given the prevalence of cloud computing: most cloud providers and platforms offer IaC tools. As the authors rightly pointed out, an IaC defect can have a devastating impact, so testing becomes crucial.

Also, the authors correctly identified that to gather methods adopted by practitioners is better to review grey literature (StackOverflow, Reddit, YouTube) than academic publications. Sadly, there's still a significant gap between academia and industry.

Cons:
There are a couple of sources that I believe could enrich the paper: books from practitioners (like https://www.terraformupandrunning.com/ ) and white papers from consulting firms (like https://www.thoughtworks.com/radar ). These two sources have the benefit of editorial review, so they can arguably have higher quality.

All of the 6 practices listed have been part of the software testing arsenal for a very long time. Static analysis (Practice I), Behaviour-Driven Development (Practice II), Isolated Environments (Practice IV), and Continuous Integration ( Practice IV), to name a few, are part of every software engineer toolkit. What/How is it different for testing IaC artefacts? Without making that point, the value of the work for both researchers and practitioners is diluted. I believe the authors should make that question a key driver of the paper.

Finally, there are some inaccuracies. Terratest is NOT language-dependent and supports multiple platforms (a claim made in Page 5), and linting/static analysis is available in almost every platform independent of the testing framework (another claim in Page 5).



----------------------- REVIEW 2 ---------------------
SUBMISSION: 2
TITLE: Testing Practices for Infrastructure as Code
AUTHORS: Mohammed Mehedi Hasan, Farzana Ahamed Bhuiyan and Akond Rahman

----------- Overall evaluation -----------
SCORE: 1 (weak accept)
----- TEXT:
Summary
The paper describes a study on IaC testing practices. The study is based on 50 internet artifacts and groups testing practices into six categories: avoiding coding anti-patterns, behavior-focused test coverage, remote testing, sandbox testing, testing every IaC change, and use of automation.  The paper also presents implications for practitioners and researchers.

Pros
-The paper presents an interesting study on an increasingly important software engineering domain.
-The study is performed using principled techniques.

I enjoyed the paper and found the study interesting. In the rest of my review, I include my main comments.

I appreciate that the paper reports the list of tools that practitioners use in their testing practices. However, it would be great to also have a theoretical description of the techniques characterizing the tools.

The paper does a good job of reporting the implications for researchers and practitioners.

I would like to see a more thorough discussion on the selection of the study artifacts. More precisely, only 223 out of 900 identified artifacts are unique results. This result does not inspire confidence in the quality of the keywords used to search for artifacts. The paper should discuss why there is a large number of duplicates.


Minor comments
-Describe axes in Figure 1.
-Footnote 3 could be a reference.
-The description of Figure 2 and Figure 3 could be improved. It is currently difficult to understand what each code entity in the script does.
-I would like to see a motivation on why 50 results (and not a different number) were considered at line 287.
-The section about rater verification (line 490) could be moved to line 331.
-The threats to validity discussion could be a section on its own.



----------------------- REVIEW 3 ---------------------
SUBMISSION: 2
TITLE: Testing Practices for Infrastructure as Code
AUTHORS: Mohammed Mehedi Hasan, Farzana Ahamed Bhuiyan and Akond Rahman

----------- Overall evaluation -----------
SCORE: 1 (weak accept)
----- TEXT:
-== Summary ==-
The paper presents an informal survey of testing practices times of the Ansible programming language. A number of practices are presented as a result of the search.

-== General comments ==-
Overall, I have enjoyed reading the paper. Although I am absolutely not familiar with the techniques presented in the paper, I did find the article interesting and worth presenting at the workshop.

The paper can be made stronger by being more rigorous with the employed terminology. For example, having a clear definition and an example of what is “Infrastructure as code” would help. Figure 2 and 3 are unfortunately not sufficient at telling the reader what could be a good vs bad practice on Ansible code. Maybe you can propose a running example that you use to illustrate the testing practices.

Soundness: Some aspects of the methodology could be formalized in a better way. In a future work, I suggest the authors to follow a “multifocal literature review” to include both peer reviewed and grey literature.

Significance: The work presents some testing practices that seem relevant for the field. Although the practices are not really surprising (but I may be wrong since I am not expert in IaC), they seems to be a valuable input for practitioners.

Verifiability: Due to the informality of the search of “Internet artifacts” it is unlikely that the process is reproducible.

Presentation: The paper is relatively easy to read and well presented. Notwithstanding, I recommend the authors to improve its presentation by being more accurate with the employed terms.

Strengths:
        + interesting paper
        + seem to give a result valuable to practitioners

Weaknesses:
        - writing can be improved on some part.

-== Specific comments ==-
Figure 1 is very informal and does not really make a strong point. I suggest to remove it. It will make the paper shorter without removing anything valuable from it.

Lines 323: “who has six years of professional experience in software engineering” => you can remove it as it is very informal and cannot support any conclusions.



----------------------- REVIEW 4 ---------------------
SUBMISSION: 2
TITLE: Testing Practices for Infrastructure as Code
AUTHORS: Mohammed Mehedi Hasan, Farzana Ahamed Bhuiyan and Akond Rahman

----------- Overall evaluation -----------
SCORE: -1 (weak reject)
----- TEXT:
This paper examines the process of Infrastructure as Code (IaC), focusing on how people test IaC code in practice.  The approach to gathering data is a search of Web pages and blog posts, since they observe that most of the information obtainable is in such forums rather than in e.g. papers. The paper describes an approach where the authors derived a set of search queries for google, collecting the top results as ranked by Google for each query.  The authors then read the results manually and distilled a series of recommendations.

This is fine as far as it goes, but there are two ways they could have gone further.

The first is there was no effort to apply NLP techniques to reading the documents.  While manual reading had advantages, it surely limits the scalability of the approach.  And there has been lots of work using pretrained models like Bert, Roberta, and Universal Sentence Embedding (USE) to understand text that has shown promising results in query answering.  While there is no guarantee it would produce good results in this domain, it is disappointing it was not even tried.  Even if the pretrained models are insufficient by themselves, they also have ability to be further specialized based on labeled data, and one could imagine taking the results they derived manually and using those to further train language models which could could then be run on a large-scale search for documents.  All in all, it would be nice if they had tried automated techniques, since there is a limit to how much can be done by hand.

The second issue that I had is the rather generic nature of the recommendations.  For instance, "avoiding Coding Anti-patterns" is surely good advice, but it seems rather obvious and it is not clear how it is specific in any way to IaC.  Similarly, "Test Every IaC Change" again seems like good advice, but it is a general philosophy of continuous testing, which is widely practiced in all sorts of domains and does not seem specific to IaC.  "Use of Automation" raises the same issues, as it is widely considered good advice in a wide range of domains.



----------------------- REVIEW 5 ---------------------
SUBMISSION: 2
TITLE: Testing Practices for Infrastructure as Code
AUTHORS: Mohammed Mehedi Hasan, Farzana Ahamed Bhuiyan and Akond Rahman

----------- Overall evaluation -----------
SCORE: 0 (borderline paper)
----- TEXT:
The paper describes a research on a particularly important emerging field - IaC testing. Even though authors provide the reader with a precise contribution, the research as it is, appears to be very introductory one, giving to authors and the surrounding community preliminary conclusions intended to lead them to the future bigger steps.

Regarding the presentation of the research and the results my main concern is that a research paper should be a self-contained text that enables a reader to read it in one flow without jumping to other sources to obtain additional information. Therefore, having in mind space limitation, I would expect a little reorganisation of the paper. For example:
- In the introduction, ln. 63 - 67, tools, syntax and scripts are mentioned, while the reader has to wait until the following section to see the example. Maybe it would be useful, at this place, to point to the examples in the background section so that it is announced to the reader.
- The background section should provide the reader with deeper information about IaC, specifics of the scripts, specifics of available tools, what can/should be tested, what are specific goals, problems and challenges in testing it, how does it relate to the "usual" program testing, etc. Furthermore, analysis of generally applied testing practices and their applicability on IaC might help to predefine a set of expected practices to be recognized in IaC testing. However, I would propose to separate this section from the related work, which could also make an additional space in the paper.
- Related work is comprehensive having in mind number of observed researches. However, the comparison to the actual research is rather informative.
- Regarding the results, it would be interesting to see interconnections between recognized practices.
- Additionally, introducing specific terms before/on their usage in the text might improve readability and the reading flow continuity. E.g. open coding, close codding, Cohen's Kappa, etc. what is it, why is it used, what do you get with it...all in all why this choice, why not something else.

Finally, for some future research I would be happy to see corresponding and deeper results derived from practice, especially encompassing testing as a whole, with possible relationships and dependences.

