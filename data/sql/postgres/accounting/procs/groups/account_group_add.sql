create or replace function account_group_add (
    p_client_id clients.clients.id%type,
    p_group_id accounting.account_groups.id%type,
    p_name accounting.account_groups.name%type,
    p_description accounting.account_groups.description%type
)
returns void
as $$
begin
    insert into accounting.account_groups (
        id,
        client_id,
        name,
        description
    ) values (
        p_group_id,
        p_client_id,
        p_name,
        p_description
    );

    -- account group tree
    insert into accounting.account_group_tree (
        client_id,
        group_id,
        path
    ) values (
        p_client_id,
        p_group_id,
        text2ltree('root.' || replace(p_group_id::text, '-', '_'))
    );
end
$$
language plpgsql;