# Manual Regression Test Checklist

## LINE member flows
- [ ] Initial registration guidance is returned
- [ ] Member registration completes
- [ ] My Page shows member information
- [ ] Payment status can be viewed
- [ ] Expense application flow completes
- [ ] Anonymous suggestion can be submitted
- [ ] Activity / event information can be viewed

## Admin authentication
- [ ] Non-admin users cannot access management functions
- [ ] Admin can generate a signed login URL
- [ ] Expired login token is rejected
- [ ] Valid login creates a session
- [ ] Protected routes reject unauthenticated access

## Member management
- [ ] Member list opens
- [ ] Search works
- [ ] Filters work
- [ ] Member detail opens

## Collections / payments
- [ ] Collection can be created
- [ ] Payment status can be updated
- [ ] Paid amount is reflected in totals
- [ ] Overdue / upcoming counts are correct

## Expenses
- [ ] Pending expenses are listed
- [ ] Expense can be approved
- [ ] Expense can be rejected
- [ ] Approved expense is reflected in accounting totals

## Accounting
- [ ] Expected amount is correct
- [ ] Collected amount is correct
- [ ] Uncollected amount is correct
- [ ] Approved expenses are included
- [ ] Current balance is correct

## Before deployment
- [ ] Confirm database backup
- [ ] Review changed files
- [ ] Run relevant regression checks
- [ ] Confirm environment variables
- [ ] Confirm main LINE and admin flows after deployment
