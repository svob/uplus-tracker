import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uplus.settings")
    try:
        import django
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )

    from django.contrib.auth.models import Group, Permission, User
    from tracker.models import IssueState, IssueCategory

    superuser, created = Group.objects.get_or_create(name='superuser')
    staff, created = Group.objects.get_or_create(name='staff')
    permissions = []
    permissions.append(Permission.objects.get(codename='add_issuestate'))
    permissions.append(Permission.objects.get(codename='change_issuestate'))
    permissions.append(Permission.objects.get(codename='delete_issuestate'))
    permissions.append(Permission.objects.get(codename='add_issuecategory'))
    permissions.append(Permission.objects.get(codename='change_issuecategory'))
    permissions.append(Permission.objects.get(codename='delete_issuecategory'))
    permissions.append(Permission.objects.get(codename='add_issue'))
    permissions.append(Permission.objects.get(codename='change_issue'))
    permissions.append(Permission.objects.get(codename='delete_issue'))

    for permission in permissions:
        superuser.permissions.add(permission)
        superuser.permissions.add(permission)

    User.objects.create_user('suTest', password='Password1*', is_staff=True).groups.add(superuser)
    User.objects.create_user('staffTest', password='Password1*').groups.add(staff)

    IssueCategory(category='Bug').save()
    IssueCategory(category='Vylepšení').save()
    IssueCategory(category='Dokumentace').save()

    IssueState(state='TODO').save()
    IssueState(state='In progress').save()
    IssueState(state='Done').save()