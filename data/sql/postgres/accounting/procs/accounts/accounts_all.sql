create or replace function accounts_all (
    p_client_id clients.clients.id%type
)
returns table (
    id accounting.accounts.id%type,
    active accounting.accounts.active%type,
    created_ts accounting.accounts.created_ts%type,
    type_id accounting.accounts.type_id%type,
    name accounting.accounts.name%type,
    description accounting.accounts.description%type
)
as $$
begin
    return query
    select
        a.id,
        a.active,
        a.created_ts,
        a.type_id,
        a.name,
        a.description
    from accounting.accounts a
    where a.client_id = p_client_id;
end
$$
language plpgsql;