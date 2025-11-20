from django.core.management.base import BaseCommand
from library.models import Book


class Command(BaseCommand):
    help = 'Update book statuses based on available copies (only mark as borrowed when no copies available)'

    def handle(self, *args, **options):
        books = Book.objects.all()
        updated_count = 0
        
        for book in books:
            old_status = book.status
            # Trigger save to update status based on new logic
            book.save()
            if old_status != book.status:
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Updated "{book.title}": {old_status} -> {book.status} '
                        f'({book.available_copies}/{book.total_copies} copies)'
                    )
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully updated {updated_count} book(s). '
                f'Total books processed: {books.count()}'
            )
        )

