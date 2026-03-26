# 🐼 Skill | Pandas Vectorized Pro
> **Version:** v3.1.5 "Solidity Guard"
> **Agent:** DATA_SCIENTIST

## Objective
Optimize data cleaning and transformation workflows using vectorized operations to maximize memory efficiency.

## Best Practices
- **No Loops:** Avoid `for` loops on DataFrames. Use `.apply()`, `.map()`, or native NumPy vectorization.
- **Memory Optimization:** Use appropriate dtypes (int32 vs int64, categories for strings) to minimize footprint.
- **Safe Subsetting:** Always use `.loc` and `.copy()` to avoid `SettingWithCopyWarning`.
- **Validation:** Use `.merge(validate='one_to_many')` to prevent unexpected data duplication.

## Data Cleaning Guard
Reject any analysis that contains unhandled missing values or un-normalized units (Must be SI units).
