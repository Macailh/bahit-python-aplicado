# Example 1: Disease Test (as discussed earlier)
# Initial Probabilities
prob_disease = 0.01  # Probability of having the disease P(Disease)
prob_no_disease = 1 - prob_disease  # Probability of not having the disease P(No Disease)
prob_positive_given_disease = 0.99  # Probability of a positive test given disease P(Positive | Disease)
prob_positive_given_no_disease = 0.02  # Probability of a positive test given no disease P(Positive | No Disease)

# Applying Bayes' Theorem
prob_disease_given_positive = (prob_positive_given_disease * prob_disease) / ((prob_positive_given_disease * prob_disease) + (prob_positive_given_no_disease * prob_no_disease))

print(f"Example 1 - Probability of having the disease given a positive test result: {prob_disease_given_positive:.2f}")

# Example 2: Spam Filter
# Suppose we have an email filter that classifies emails as spam or not spam.
# Let's assume the following probabilities based on historical data:
# P(Spam) = 0.3, P(Not Spam) = 0.7
# P(Word | Spam) = 0.8, P(Word | Not Spam) = 0.1
# We received an email containing a specific word, what is the probability that it is spam?

prob_spam = 0.3  # P(Spam)
prob_not_spam = 0.7  # P(Not Spam)
prob_word_given_spam = 0.8  # P(Word | Spam)
prob_word_given_not_spam = 0.1  # P(Word | Not Spam)

# Applying Bayes' Theorem
prob_spam_given_word = (prob_word_given_spam * prob_spam) / ((prob_word_given_spam * prob_spam) + (prob_word_given_not_spam * prob_not_spam))

print(f"Example 2 - Probability of an email being spam given it contains a specific word: {prob_spam_given_word:.2f}")

# Example 3: Drug Testing
# Consider a drug test that is 95% accurate in identifying drug use and 90% accurate in identifying non-use.
# Assume 5% of a population uses drugs.
# What is the probability that a person uses drugs given that they tested positive?

prob_drug_use = 0.05  # P(Drug Use)
prob_no_drug_use = 1 - prob_drug_use  # P(No Drug Use)
prob_positive_given_drug_use = 0.95  # P(Positive | Drug Use)
prob_positive_given_no_drug_use = 0.10  # P(Positive | No Drug Use)

# Applying Bayes' Theorem
prob_drug_use_given_positive = (prob_positive_given_drug_use * prob_drug_use) / ((prob_positive_given_drug_use * prob_drug_use) + (prob_positive_given_no_drug_use * prob_no_drug_use))

print(f"Example 3 - Probability of drug use given a positive test result: {prob_drug_use_given_positive:.2f}")
