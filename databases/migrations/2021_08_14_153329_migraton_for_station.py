"""MigratonForStation Migration."""

from masoniteorm.migrations import Migration


class MigratonForStation(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("stations") as table:
            table.increments("id")
            table.string("name")
            table.unsigned("ip")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("stations")
