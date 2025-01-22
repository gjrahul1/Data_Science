#### Explaining the Co-relation between Stastical Analysis and Effect Size

1. **T-test for p-values**: 
   - The t-test evaluates whether the means of two groups are statistically significantly different from each other. 
   - A p-value greater than 0.05 (for a significance level \(\alpha = 0.05\)) suggests that there is no statistically significant difference between the groups.

2. **Pearson correlation coefficient for effect size**:
   - While the t-test assesses whether a difference exists, it does not provide information about the *magnitude* or *practical significance* of the relationship or difference.
   - The Pearson correlation coefficient (denoted as \(r\)) quantifies the strength and direction of the linear relationship between two variables. When used as an effect size measure in the context of t-tests, it reflects how strongly the two groups differ relative to their variability.

### Why Check Both?
1. **Statistical significance vs. Practical significance**:
   - A non-significant p-value (\(p > 0.05\)) might occur even if there is a small effect, especially in cases with small sample sizes or high variability. The Pearson coefficient provides additional context by quantifying the strength of the effect, regardless of its statistical significance.

2. **Insight into the relationship**:
   - The Pearson coefficient is particularly useful when we want to understand how strongly the variables are associated. For example, in linear assumptions, it gives insight into the strength of the linear relationship, which might not be evident from the t-test alone.

3. **Complementary Measures**:
   - The t-test tells us whether to reject the null hypothesis, while the Pearson correlation coefficient provides a measure of effect size, aiding in interpreting the results. A study might fail to achieve statistical significance but still show a moderate to strong correlation, which could be meaningful in practical terms.

### Conclusion
Using the Pearson coefficient alongside the t-test for p-values allows for a more comprehensive understanding of the data. It addresses both whether a difference exists (t-test, significance testing) and the extent or strength of the relationship (Pearson coefficient, effect size).
