----------------------- REVIEW 1 ---------------------
SUBMISSION: 310
TITLE: An Exploratory Synthesis of Testing Practices for Infrastructure as Code
AUTHORS: Mohammed Mehedi Hasan, Farzana Ahmed Bhuiyan and Akond Rahman

----------- Overall evaluation -----------
SCORE: -2 (reject)
----- TEXT:
-> Summary of the submission.
This short paper presents a non-systematic grey literature review of 50 internet websites aiming at analyzing the developer's practices concerning to infrastructure code (IaC) testing. Two researchers employed an open-coding procedure which led to the emergence of six tactics currently employed by practitioners when testing infrastructure code.

-> Comments for authors.
The paper treats a timely and relevant problem, which is indeed currently under-investigated. The idea of analyzing the grey literature is a good one, given the fact that only a few research papers are available. Besides these good points, I consider this paper pretty weak for a number of reasons that I try to explain further in the following.

(1) The NIER track is dedicated to "promising ideas in the early stages of research". The proposed paper does not seem to fit the goals of the track, since it is neither an idea nor an early research on the topic of infrastructure code testing. Indeed, the study represents a substantial step forward the currently available literature on the matter and, as such, would deserve much more space than a short paper to be conveyed in an appropriate manner.

(2) The topic of infrastructure code maintenance and evolution is relatively new - indeed, a very few papers on the topic have been published so far. Even for a short paper, I would recommend the inclusion of some background information on the topic: as an example, from the paper it remains unclear (i) what infrastructure code actually is, (ii) why it is relevant nowadays, and (iii) the motivations why quality aspects are important in this context. These pieces of information would be needed for a reader interested in getting more from the paper.

(3) The methodological steps presented in the paper lack of details. This is likely due to space limitation, however even short papers should be self-contained and comprehensive. Again, the major problem of this paper is that it should not be considered as a short paper. Some examples of methodological choices that are not well motivated or even absent are:

- Is this study a systematic grey literature review? Does it follow existing guidelines?

- Search query: the paper exploits various strings. Can they retrieve all possible sources? Are there terms that can be seen as synonyms of testing, e.g., validation/verification, that should be included? If not, why?

- Data collection: the paper collects the first 100 search results from Google. Were there additional pages that have not been considered? If yes, why were they discarded? Which kind of information has been lost?

- Data collection: was the procedure done activating the 'incognito' mode? If not, the search process may be biased because of personal preferences.

- Filtering procedure: likely, not all blogs/websites considered were reliable, e.g., some of them might be written by people with no experience on the matter. How does this paper treat this aspect?

- Quality assessment: more in general, how was the quality evaluation of the sources retrieved done?

All these aspects should be considered and described in the paper. Of course, this would take more space, space that cannot really be found within a short paper.

(4) The vision section should describe the main implications of the work. While I appreciate that the paper tries to define them, they do not seem to be actionable. The ultimate goal of a literature review is to define a roadmap for future research on the matter. In this sense, the paper fails in doing that. Just to provide some examples of the aspects that remain unclear after reading the paper:

- Are there tools available in research that may be useful to test infrastructure code?

- How can the research community practically contribute to helping practitioners? The paper mentions something, but these are described at a too high-level. For instance, "researchers can investigate to what extent existing GPL testing research is applicable for IaC": this is good, but how? What are the next practical steps to be done?

- According to the paper, the list of practices described in the paper is not complete. I wonder why, what is missing and how they can be completed by further research.

All in all, I think the paper has an enormous potential and will surely influence the research community. Yet, a NIER track is the wrong venue for a paper like this one. I strongly recommend to submit the work somewhere else, for instance to a journal that gives more space to elaborate on the methodology employed, the results achieved, and the practical future avenues to follow in the research field. Based on my comments, I recommend the rejection of the paper.



----------------------- REVIEW 2 ---------------------
SUBMISSION: 310
TITLE: An Exploratory Synthesis of Testing Practices for Infrastructure as Code
AUTHORS: Mohammed Mehedi Hasan, Farzana Ahmed Bhuiyan and Akond Rahman

----------- Overall evaluation -----------
SCORE: 1 (weak accept)
----- TEXT:
Pros:
- Relevant topic for the software engineering community
- List of future directions for practitioners and researchers
- Easy to read paper

Cons:
- Comparison to related work is a bit superficial
- Some details about the coding process are not described


The paper presents a review of internet artifacts with the purpose of identifying testing practices reported by practitioners when referring to Infrastructure as Code scripts. In particular, 50 artifacts were analyzed after filtering an initial list of 800 links retrieved by google. The links were retrieved with 8 search queries. The practices were identified by using open coding, and after presenting the practices, the authors report a list of future directions for practitioners and researchers.

The paper is easy to read and presents an interesting topic. As a NIER paper I think it accomplishes the goal because it explores a topic and proposes a list of future directions that could lead to an interesting discussion when presented at ICSME.

I only have minor recommendations that are described as follows:

- Section 1: “The goal of this paper is to help practitioners improve the quality of infrastructure as code (IaC) scripts by deriving a set of testing practices for IaC scripts” IMHO, the term “deriving” does not properly describe what was done. I think that “identifying” is better.

- Section 1: “We answer the following research question: What testing practices can be used for infrastructure as code scripts?” I think “can be used”  implies analyzing the existing testing practices (in general) and assess whether those techniques can be also used to IaC scripts, however, the study did not do that. In that sense, I suggest to replace “can be used” with “are used”, or specify in the RQ that  it is according to practitioners point of view, e.g., “What testing practices can be used for infrastructure as code scripts according to practitioners?”

- The mapping study by Rahman et al. [12] presents that testing IaC is one of the topics discussed in the reviewed papers.  However, the approaches presented in those papers reviewed at [12], are not discussed in the NIER paper. Thus, my recommendation is to include in II-B a discussion about how the results in this NIER paper are complementary to the papers and findings reported in [12]. In addition, [12] has a “5.3. Potential Research Avenues in IaC ” section; please complement your Vision section with the discussion in Section 5.3 of [12].

- Section III-A: “the second author of the paper, who applies closed coding [26] on the collected 50 Internet artifacts”. At this point the reader does not know that “50” is the final number of artifacts after filtering.

- Section III-B: “Next, we read each of the 223 artifacts and identify 50 artifacts to actually discuss IaC testing practices.” Please provide more details about how was the filtering done. Was it done by the first author? All the authors?

- Section III-B-IV: “The quality of the test cases are evaluated based on how much they cover the expected behavior” Could you elaborate more on how to measure the coverage of expected behavior? Or are you talking about IaC script code coverage?

- Section III-B-V: Could you describe the “incomplete conditional” anti-pattern?

- The “Rater verification” part in section III looks disconnected from the rest. I suggest moving this part to Section III.A

- Were there any conflicts resolution step? Please elaborate more on that. Also, could you provide more details about the reasons for the disagreement between the raters?

- Check the references. I found cases in which the same paper is reported as 2 different references, e.g., [2] and [6], and [1] and [14].



----------------------- REVIEW 3 ---------------------
SUBMISSION: 310
TITLE: An Exploratory Synthesis of Testing Practices for Infrastructure as Code
AUTHORS: Mohammed Mehedi Hasan, Farzana Ahmed Bhuiyan and Akond Rahman

----------- Overall evaluation -----------
SCORE: -1 (weak reject)
----- TEXT:
Pros:
1.This paper is well written and easy to follow
2.The problem resolved in this paper is important

Cons:
1.This paper is not innovative enough
2.Some practices are not convincing enough


In this paper, the authors apply qualitative analysis on 50 Internet artifacts to understand the IaC test practices. Basically, the authors collected Internet artifacts via seven search strings and applied some filters to discard the duplicate ones and the ones do not explicitly discuss IaC testing. Then two authors read these artifacts and concluded six testing practices from them.

Overall, this paper is well written and easy to follow. But the scope of this paper does not perfectly match the scope of ICSME NIER track. It provides some useful practices for practitioners and researchers, but it is not innovative enough. The design of this study is quite similar as paper [10].

Moreover, some practices are not convincing enough. For example, only 4 Internet artifacts mentioned the sixth practice – remote testing, which is hard to demonstrate the importance of this practice, and the state from one practitioner [32] does not emphasize remote testing is the key of running the tests on real systems.


