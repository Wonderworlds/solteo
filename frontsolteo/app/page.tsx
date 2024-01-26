'use client';

import axios, { AxiosResponse } from 'axios';
import React from 'react';
import { IconContext } from 'react-icons';
import { AiFillLeftCircle, AiFillRightCircle } from 'react-icons/ai';
import ReactPaginate from 'react-paginate';
import Filter from './components/filter';
import Record, { RecordProps } from './records/record';

const client = axios.create({
  baseURL: 'https://data.enedis.fr/api/v2/',
  timeout: 1000,
});

const orders = ['desc', 'asc'];
const filters = ['production', 'injection', 'MW', 'Année'];
const filters_query = ['type_production', 'type_injection', 'mw', 'annee'];

export default function Home() {
  const [records, setRecords] = React.useState<RecordProps[]>([]);
  const [page, setPage] = React.useState<number>(0);
  const [rowNumber, setRowNumber] = React.useState<number>(20);
  const [fixedRowNumber, setFixedRowNumber] = React.useState<number>(20);
  const [totalRow, setTotalRow] = React.useState<number>(0);
  const [filterClicked, setFilterClicked] = React.useState<number>(0);
  const [order, setOrder] = React.useState<number>(0);
  const [timeoutId, setTimeoutId] = React.useState<NodeJS.Timeout>();
  const [reload, setReload] = React.useState<boolean>(false);

  React.useEffect(() => {
    const query = {
      params: {
        Name: '0ce8196c-e2f7-4405-a64c-103f5c284387',
        order_by: filters_query[filterClicked] + ' ' + orders[order],
        select: 'annee,type_production,type_injection,mw',
        limit: fixedRowNumber,
        offset: page * fixedRowNumber,
      },
    };

    client
      .get('catalog/datasets/fa-sorties/records', query)
      .then((res: AxiosResponse) => {
        const data_records: unknown[] = res.data.records;
        console.log(res);
        setTotalRow(res.data.total_count);
        const record_formatted: RecordProps[] = data_records.map((elt: any) => {
          return {
            year: elt.record.fields.annee,
            date: new Date(elt.record.timestamp).toLocaleDateString(),
            type_production: elt.record.fields.type_production,
            type_injection: elt.record.fields.type_injection,
            mw: elt.record.fields.mw,
          };
        });
        setRecords(record_formatted);
      })
      .catch((err) => {
        console.log(err);
      });
  }, [page, filterClicked, order, fixedRowNumber]);

  function handleFormInputChange(e: React.ChangeEvent<HTMLInputElement>) {
    if (e.target.value === '') return;
    let value = parseInt(e.target.value);
    if (timeoutId || timeoutId !== undefined) {
      clearTimeout(timeoutId);
      setTimeoutId(undefined);
    }
    value = value > 100 ? 100 : value;
    value = value < 1 ? 1 : value;
    setRowNumber(value);
    const timeout = setTimeout(() => {
      setFixedRowNumber(value);
      setRowNumber(value);
    }, 1000);
    setTimeoutId(timeout);
  }

  return (
    <main className="page">
      <div className="divPage">
        <h1 className="pageTitle">
          Projets en développement - Sorties des demandes - Evolution: {totalRow}
        </h1>
        <div className="pageFilter">
          {filters.map((filter, index) => (
            <Filter
              key={index}
              self={index}
              name={filter}
              isClicked={filterClicked}
              setIsClicked={setFilterClicked}
            />
          ))}
          {orders.map((val, index) => (
            <Filter key={index} name={val} isClicked={order} setIsClicked={setOrder} self={index} />
          ))}
          <div className="pageFilterForm">
            <label htmlFor="pageFilterFormInput">lignes</label>
            <div className="pageFilterFormInput">
              <input
                id="pageFilterFormInput"
                type="number"
                placeholder="10 - 100"
                max={100}
                min={0}
                value={rowNumber}
                onChange={(e) => handleFormInputChange(e)}
              />
            </div>
          </div>
        </div>
        <div className="pageRecords">
          {records.length > 0 ? (
            records.map((record, index) => <Record key={index} {...record} />)
          ) : (
            <div className="loading">Loading...</div>
          )}
        </div>
        <div className="pagePagination">
          <ReactPaginate
            containerClassName="pagination"
            onPageChange={(e) => {
              setPage(e.selected);
            }}
            pageRangeDisplayed={3}
            marginPagesDisplayed={2}
            pageCount={Math.ceil(totalRow / fixedRowNumber)}
            previousLabel={
              <IconContext.Provider value={{ color: '#B8C1CC', size: '36px' }}>
                <AiFillLeftCircle />
              </IconContext.Provider>
            }
            nextLabel={
              <IconContext.Provider value={{ color: '#B8C1CC', size: '36px' }}>
                <AiFillRightCircle />
              </IconContext.Provider>
            }
            pageClassName="page-item"
            pageLinkClassName="page-link"
            previousClassName="page-item"
            previousLinkClassName="page-link"
            nextClassName="page-item"
            nextLinkClassName="page-link"
            breakLabel="..."
            breakClassName="page-item"
            breakLinkClassName="page-link"
            activeClassName="active"
            renderOnZeroPageCount={null}
          />
        </div>
      </div>
    </main>
  );
}
