# Titles of News Articles
Classifying news articles into 9 categories using their titles.

Possible categories are:
- verslas
- sportas
- kultura
- mokslas-ir-it
- nuomones
- eismas
- kriminalai
- sveikata
- muzika

## Final model:
- Logistic regression, using vectorized titles, their length and word count
- 87.481 % accuracy and 87.487 % f1 scores

#### Conclusion
Reached results show that titles differ from one category to another, so they can be successfully classified.
It may be harder to reach better results due to the fact that titles from different categories can have
very similar topics and in reality they might be assigned to multiple categories.

## Predicting categories of titles
1. Launching app.py
2. Opening the generated link in a browser
3. Providing the title in a text submission field
4. The predicted category for the title is then displayed

##Additional requirement for web scraping:
Installing the firefox browser.
