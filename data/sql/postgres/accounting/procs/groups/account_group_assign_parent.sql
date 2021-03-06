create or replace function account_group_assign_parent (
    p_client_id clients.clients.id%type,
    p_group_id accounting.account_groups.id%type,
    p_parent_group_id accounting.account_groups.id%type
)
returns void
as $$
declare
    t_parent_path public.ltree;
    t_new_path public.ltree;
    t_old_path public.ltree;
begin
    -- get parent path
    select
        a.path into t_parent_path
    from accounting.account_group_tree a
    where a.client_id = p_client_id
        and a.group_id = p_parent_group_id;

    -- get current path
    select
        a.path into t_old_path
    from accounting.account_group_tree a
    where a.client_id = p_client_id
        and a.group_id = p_group_id;

    t_new_path := text2ltree(ltree2text(t_parent_path) || '.' || replace(p_group_id::text, '-', '_'));

    update accounting.account_group_tree set
        parent_group_id = p_parent_group_id,
        path = t_new_path
    where client_id = p_client_id
        and group_id = p_group_id;

    -- update descendants
    update accounting.account_group_tree a set
        path = t_new_path || subpath(b.path, nlevel(t_old_path))
    from accounting.account_group_tree b
    where a.client_id = p_client_id
        and b.client_id = p_client_id
        and b.path <@ t_old_path
        and nlevel(b.path) > nlevel(t_old_path)
        and a.group_id = b.group_id;
end
$$
language plpgsql;
