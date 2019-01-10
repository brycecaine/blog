title: Crispy Forms and Django Formsets
date: 2019-01-09
tags: forms, crispy-forms, django
summary: How to make sure form tags are proper when adding a crispy-form formset to an existing crispy form in a django template

The other day I attempted to add `{% crispy formset %}` to my an existing form in my html (within a form tag). Crispy form's default behavior was to add a form tag when rendering its html. This caused a conflict of form tags.

The formset was generated using `inlineformset_factory`, which doesn’t have a `form_tag` parameter. So I created a form with an __init__ method and set the `helper.form_tag` variable to False. Then I passed that form into the `inlineformset_factory`, and it resolved the issue.

The reason I'm documenting this is that the initial symptom was that after I had added `{% crispy formset %}` at first, the form wouldn’t submit or even trigger the missing-field js boxes. The behavior was ellusive to troubleshoot. Hope this helps someone else too.
